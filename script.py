name: Daily Python Script
on:
  schedule:
    - cron: '0 9 * * *'
  workflow_dispatch:
jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Run daily script
        run: |
          python << 'SCRIPT'
          import datetime
          print(f'Daily script executed at {datetime.datetime.now()}')
          print('Performing daily tasks...')
          SCRIPT
EOF
