name: CI MS6

on:
  push:
    branches:
      - main
      - develop
    paths:
      - 'EC03P1_MI202628_UrbanHub/**'
      - '.github/workflows/ci_ms6.yml'

  pull_request:
    branches:
      - main
      - develop
    paths:
      - 'EC03P1_MI202628_UrbanHub/**'
      - '.github/workflows/ci_ms6.yml'

jobs:
  flake8:
    name: Flake8
    runs-on: ubuntu-latest

    defaults:
      run:
        working-directory: EC03P1_MI202628_UrbanHub/project

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Install Poetry
        run: pip install "poetry==2.3.2"

      - name: Sync lock file with pyproject
        run: poetry lock

      - name: Install dependencies
        run: poetry install --no-interaction

      - name: Run flake8
        run: |
          pip install flake8
          flake8 . --max-line-length=120 --extend-ignore=W292,W391

  sonarqube:
    name: SonarCloud
    runs-on: ubuntu-latest
    needs: flake8

    defaults:
      run:
        working-directory: EC03P1_MI202628_UrbanHub/project

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Install Poetry
        run: pip install "poetry==2.3.2"

      - name: Install dependencies
        # Note: J'ai enlevé 'poetry lock' pour gagner du temps, le lock doit être dans ton repo.
        run: poetry install --no-interaction

      - name: Run tests with coverage XML
        env:
          PYTHONPATH: src
        run: |
          mkdir -p reports
          # On lance pytest. On s'assure que le rapport est généré à la racine du working-directory
          poetry run pytest -q --cov=src --cov-report=xml:reports/coverage.xml

      - name: Fix coverage paths for SonarCloud
        # Cette étape est CRUCIALE. Elle s'assure que les chemins dans le XML 
        # correspondent exactement à ce que Sonar attend par rapport au projectBaseDir.
        run: |
          sed -i 's@filename="src/@filename="@g' reports/coverage.xml

      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@v3
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        with:
          projectBaseDir: EC03P1_MI202628_UrbanHub/project
          args: >
            -Dsonar.projectKey=lee-rudy_ec03_urbanhub
            -Dsonar.organization=lee-rudy
            -Dsonar.sources=src
            -Dsonar.tests=tests
            -Dsonar.python.version=3.13
            -Dsonar.python.coverage.reportPaths=reports/coverage.xml
            -Dsonar.sourceEncoding=UTF-8
            -Dsonar.verbose=true
