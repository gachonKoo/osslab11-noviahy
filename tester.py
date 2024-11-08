name: Autograding Tests

on:
  push:
    branches:
      - main
  repository_dispatch:

permissions:
  checks: write
  actions: read
  contents: read

jobs:
  run-autograding-tests:
    runs-on: ubuntu-latest
    if: github.actor != 'github-classroom[bot]'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        
      - name: Run Tests
        id: run-tests
        uses: classroom-resources/autograding-io-grader@v1
        with:
          test-name: test
          command: python tester.py
          expected-output: |
            c = 5.0
            area = 314.1592653589793
          comparison-method: contains
          timeout: 10
          
      - name: Autograding Reporter
        uses: classroom-resources/autograding-grading-reporter@v1
        env:
          TEST_RESULTS: ${{ steps.run-tests.outputs.result }}
        with:
          runners: test
