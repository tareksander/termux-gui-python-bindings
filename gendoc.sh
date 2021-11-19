#!/bin/bash
cd "$(dirname "$0")"
pdoc --force --html -o docs/ src/termuxgui
