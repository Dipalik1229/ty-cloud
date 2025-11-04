name: PR Check
on:
  pull_request:
    branches: [ main ]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - name: Run checks
        run: |
          echo 'Running PR validation'
          python -m py_compile *.py
EOF
