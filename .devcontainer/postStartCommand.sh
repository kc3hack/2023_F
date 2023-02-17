#!/bin/bash

cd /usr/src/app/backend
pip install --no-cache-dir --upgrade -r ./requirements.txt

cd /usr/src/app/frontend/kc3-front
npm install --no-progress
