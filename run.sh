#!/bin/bash

git pull origin master
pip3 install -r requirements.txt

python3 src/get_data.py

jupyter nbconvert index.ipynb --to slides --SlidesExporter.reveal_scroll=True
mv index.slides.html index.html
git add .
git commit -m "added/modified/deleted stuffs."
git push origin master