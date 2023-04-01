#!/bin/sh
# Shell script to run bot with `cron`
cd ~
cd projects/twitter-project/
source venv/bin/activate
cd paulocamaraflix
python ./main.py
deactivate
cd ~