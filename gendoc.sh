#!/bin/bash
cd "$(dirname "$0")" || { echo "cd failed"; exit 1; }
pdoc --force --html -o docs/ src/termuxgui
