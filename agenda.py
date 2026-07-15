name: Update Hockey Agenda

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install -r requirements.txt

      - run: python agenda.py

      - name: Commit ICS
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add JO8-Rood.ics
          git commit -m "Nieuwe agenda" || echo "Geen wijzigingen"
          git push
