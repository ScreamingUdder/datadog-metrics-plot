from datadog import initialize, api
import time
import json
import pandas

options = {
    'api_key': '5d21d1ac7ccb1a6ca8a4a1e6986882ec', #Your API_KEY and APP_KEY, see https://app.datadoghq.com/account/settings#api
    'app_key': 'c706c18e6764af70977c3d65ee99edccaa4338a4'
}

initialize(**options)

start = int(time.time()) - 300 #Here you can specify the time period over which you want to fetch the data, it's in seconds so here we fetch 5 mins
end = start + 300

query = 'kafka.messages_in.rate{*}' #Select the metric you want to get, see your list here: https://app.datadoghq.com/metric/summary . Select the host from which you want the data, see here: https://app.datadoghq.com/infrastructure

results = api.Metric.query(start=start - 300, end=end, query=query)

f = open('out.txt', 'w') #this will create a file name out.txt in the folder you are in
print >> f, json.dumps(results)
f.close()
#print results #That should display the results in the terminal
