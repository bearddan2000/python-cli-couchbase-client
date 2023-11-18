apt update && apt install -y --no-install-recommends \
    apt-transport-https sudo \
    software-properties-common

# set -m
 
/entrypoint.sh couchbase-server &
 
sleep 15
 
# curl -v -X POST db:8091/pools/default -d memoryQuota=512 -d indexMemoryQuota=512
#  
# curl -v db:8091/node/controller/setupServices -d services=kv%2cn1ql%2Cindex
# 
# curl -v -X POST db:8091/pools/default/buckets -d name=$COUCHBASE_BUCKET -d bucketType=couchbase -d ramQuotaMB=128
# 
# curl -i -X POST db:8091/settings/indexes -d 'storageMode=memory_optimized'

curl -v db:8091/settings/web -d port=8091 -d username=$COUCHBASE_ADMINISTRATOR_USERNAME -d password=$COUCHBASE_ADMINISTRATOR_PASSWORD
 
curl -i -u $COUCHBASE_ADMINISTRATOR_USERNAME:$COUCHBASE_ADMINISTRATOR_PASSWORD -X POST db:8091/settings/indexes -d 'storageMode=memory_optimized'

curl -v -u $COUCHBASE_ADMINISTRATOR_USERNAME:$COUCHBASE_ADMINISTRATOR_PASSWORD -X POST db:8091/pools/default/buckets -d name=$COUCHBASE_BUCKET -d bucketType=couchbase -d ramQuotaMB=128 
# curl -v -u $COUCHBASE_ADMINISTRATOR_USERNAME:$COUCHBASE_ADMINISTRATOR_PASSWORD -X POST db:8091/pools/default/buckets -d name=$COUCHBASE_BUCKET -d bucketType=couchbase -d ramQuotaMB=128 -d authType=sasl -d saslPassword=$COUCHBASE_BUCKET_PASSWORD
 
# sleep 45
#  
# curl -v db:8093/query/service -d "statement=CREATE PRIMARY INDEX ON `$COUCHBASE_BUCKET`"
 