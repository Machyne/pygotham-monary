#! /bin/bash

killall mongod
rm -rf ./data
mkdir -p ./data/db
mongod --dbpath ./data/db/ --logpath ./data/log --fork

if [[ ! -f "./taxi/trip_data_small.csv" || ! -f "./taxi/trip_fare_small.csv"]]; then
    echo "note, you must fist get the taxi data from:"
    echo "http://www.andresmh.com/nyctaxitrips/"
    echo "We downloaded 1 file from each trip_data and trip_fares and took the first"
    echo "3,000,001 lines from each (3million records + the header)"
    exit 1
fi

python loader.py
mongo localhost:27017/taxi --eval "printjson(db.fares.ensureIndex({pickup_time:1}))"
mongo localhost:27017/taxi --eval "printjson(db.trips.ensureIndex({distance:1}))"