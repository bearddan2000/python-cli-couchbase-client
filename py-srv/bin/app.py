import os, pprint

# needed for any cluster connection
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

# options for a cluster and SQL++ (N1QL) queries
from couchbase.options import (ClusterOptions, QueryOptions)

BUCKET = os.getenv('COUCHBASE_BUCKET')
COLLECTION = os.getenv('COUCHBASE_COLLECTION')
INDEX = 'id'
PASSWORD = os.getenv('COUCHBASE_ADMINISTRATOR_PASSWORD')
USER = os.getenv('COUCHBASE_ADMINISTRATOR_USERNAME')

pp = pprint.PrettyPrinter(indent=4, depth=6)

# get a reference to our cluster
cluster = Cluster.connect('couchbase://db', ClusterOptions(
  PasswordAuthenticator(USER, PASSWORD)))

# get a reference to our bucket
cb = cluster.bucket(BUCKET)

sql_query = f'CREATE COLLECTION {BUCKET}.{COLLECTION}'
cluster.query(sql_query)

# get a reference to the default collection
cb_coll = cb.default_collection()

doc = [
      {'id': '0', 'type': 'airline', 'callsign': 'CBS'},
      {'id': '1', 'type': 'car', 'callsign': 'CS2'},
      {'id': '2', 'type': 'bus', 'callsign': 'B3'}
   ]

for data in doc:
   cb_coll.insert(data[INDEX], data)

sql_query = f'CREATE PRIMARY INDEX ON {BUCKET}.{COLLECTION}.{INDEX}'
cluster.query(sql_query)

# get a document
for data in doc:
   result = cb_coll.get(data[INDEX])
   print(result.content_as[dict])

results = [val for val in doc if 'CBS' in val['callsign']]

pp.pprint(results)

# using SQL++ (a.k.a N1QL) Seems to be an error or something
# call_sign = 'CBS'
# sql_query = f'SELECT type, callsign FROM {BUCKET}.{COLLECTION}.{INDEX} WHERE callsign = "{call_sign}" LIMIT 1'
# results = cluster.query(sql_query)
# 
# # iterate over rows
# for row in results:
#    # each row is an instance of the query call
#    try:
#       name = row[INDEX]["type"]
#       callsign = row[INDEX]["callsign"]
#       print(f"Airline type: {name}, callsign: {callsign}")
#    except KeyError:
#       print(f"Row does not contain '{INDEX}' key")