from datadog import initialize, api
import time
import json

# API_KEY and APP_KEY should be in a separate file called keys.txt
with open('keys.txt', 'r') as key_file:
    keys = key_file.readlines()

options = {
    'api_key': keys[0],
    'app_key': keys[1]
}

initialize(**options)

duration = 300  # seconds
end = int(time.time())
start = end - duration

# Metric to get, from this list: https://app.datadoghq.com/metric/summary
query = 'kafka.messages_in.rate{*}'

results = api.Metric.query(start=start, end=end, query=query)

f = open('out.txt', 'w')
print >> f, json.dumps(results)
f.close()

query = 'kafka.net.bytes_in.rate{*}'
results = api.Metric.query(start=start, end=end, query=query)
f = open('bytes_in.txt', 'w')
print >> f, json.dumps(results)
f.close()

query = 'kafka.net.bytes_out.rate{*}'
results = api.Metric.query(start=start, end=end, query=query)
f = open('bytes_out.txt', 'w')
print >> f, json.dumps(results)
f.close()
