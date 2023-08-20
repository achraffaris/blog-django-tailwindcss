#! /bin/bash
cd miniproject

rm -rf static/CACHE
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch