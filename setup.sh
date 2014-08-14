#! /bin/bash

killall mongod
rm -rf ./data
mkdir -p ./data/db
mongod --dbpath ./data/db/ --logpath ./data/log --fork
# note, you must fist get the taxi data from:
# http://www.andresmh.com/nyctaxitrips/
# We downloaded 1 file from each trip_data and trip_fares and took the first
# 3,000,001 lines from each (3million records + the header)
python loader.py
mongo localhost:27017/taxi --eval "printjson(db.fares.ensureIndex({pickup_time:1}))"
mongo localhost:27017/taxi --eval "printjson(db.trips.ensureIndex({distance:1}))"