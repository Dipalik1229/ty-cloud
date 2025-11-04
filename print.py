name: Print Message
on:
  push:
    branches: [ main ]
jobs:
  print:
    runs-on: ubuntu-latest
    steps:
      - name: Print custom message
        run: |
          echo '================================'
          echo 'New commit pushed successfully!'
          echo 'Timestamp: $(date)'
          echo '================================'
EOF
