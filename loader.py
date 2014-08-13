from os import path
from datetime import datetime

import pymongo

time_format = "%Y-%m-%d %H:%M:%S"


def parse_trip_data(fname):
    documents = []
    with pymongo.MongoClient() as client:
        db = client.taxi
        with open(fname, "r") as fd:
            fd.readline()
            for line in fd:
                (medallion, hack_license, vendor_id, rate_code,
                 store_and_fwd_flag, pickup_time, drop_time, passenger_count,
                 trip_time_in_secs, trip_distance, pickup_lng, pickup_lat,
                 drop_lng, drop_lat) = line.split(',')
                doc = {
                    "medallion": medallion,
                    "license": hack_license,
                    "vendor": vendor_id,
                    "rate_code": int(rate_code),
                    "pickup_time": datetime.strptime(pickup_time, time_format),
                    "drop_time": datetime.strptime(drop_time, time_format),
                    "passengers": int(passenger_count),
                    "trip_time": int(trip_time_in_secs),
                    "distance": float(trip_distance)}
                try:
                    doc["pickup_loc"] = {
                        "type": "Point",
                        "coordinates": [float(pickup_lat),
                                        float(pickup_lng)]}
                except:
                    pass
                try:
                    doc["drop_loc"] = {
                        "type": "Point",
                        "coordinates": [float(drop_lat),
                                        float(drop_lng)]}
                except:
                    pass
                documents.append(doc)
                if len(documents) >= 4000:
                    db.trips.insert(documents)
                    documents = []
            if len(documents) != 0:
                db.trips.insert(documents)


def parse_trip_fare(fname):
    documents = []
    with pymongo.MongoClient() as client:
        db = client.taxi
        with open(fname, "r") as fd:
            fd.readline()
            for line in fd:
                (medallion, hack_license, vendor_id, pickup_time, payment_type,
                 fare_amount, surcharge, mta_tax, tip_amount, tolls_amount,
                 total_amount) = line.strip().split(",")
                doc = {
                    "medallion": medallion,
                    "license": hack_license,
                    "vendor": vendor_id,
                    "pickup_time": datetime.strptime(pickup_time, time_format),
                    "payment_type": payment_type,
                    "fare_amount": float(fare_amount),
                    "surcharge": float(surcharge),
                    "mta_tax": float(mta_tax),
                    "tip_amount": float(tip_amount),
                    "tolls_amount": float(tolls_amount),
                    "total_amount": float(total_amount)
                }
                documents.append(doc)
                if len(documents) >= 4000:
                    db.fares.insert(documents)
                    documents = []
            if len(documents) != 0:
                db.fares.insert(documents)


data_files = ['trip_data_small.csv']
fare_files = ['trip_fare_small.csv']


if __name__ == '__main__':
    with pymongo.MongoClient() as client:
        print('Removing old database.')
        client.drop_database('taxi')
    print('Inserting new documents...')
    for fname in data_files:
        print('\tParsing %s' % fname)
        parse_trip_data(path.join('taxi', fname))
    for fname in fare_files:
        print('\tParsing %s' % fname)
        parse_trip_fare(path.join('taxi', fname))
    print('Done.')
