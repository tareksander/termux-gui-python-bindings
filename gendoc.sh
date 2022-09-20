#!/bin/bash
cd "$(dirname "$0")" || { echo "cd failed"; exit 1; }
# pypi package: sphinx
sphinx-build -b html docsource/ docs/
