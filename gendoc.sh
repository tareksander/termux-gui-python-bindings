#!/bin/bash
cd "$(dirname "$0")"
pdoc --force --html -o doc/ src/termuxgui
