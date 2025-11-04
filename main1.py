name: Monday Greeting
on:
  schedule:
    - cron: '0 8 * * 1'
  workflow_dispatch:
jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Print greeting
        run: echo 'Hello DevOps'
EOF
