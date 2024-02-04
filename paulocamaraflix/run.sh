#!/bin/sh
# Shell script to run bot with `cron`
cd ~
cd projects/twitter-project/
source env/bin/activate
cd paulocamaraflix
python3 ./main.py
deactivate
cd ~