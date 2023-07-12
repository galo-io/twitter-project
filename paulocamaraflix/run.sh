#!/bin/sh
# Shell script to run bot with `cron`
cd ~
cd projects/
source venv/bin/activate
cd twitter-project/paulocamaraflix
python ./main.py
sleep 300
python ./main_review.py
deactivate
cd ~
