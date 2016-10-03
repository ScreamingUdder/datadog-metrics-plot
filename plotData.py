import json
import pprint
from pandas.io.json import json_normalize
import seaborn
import matplotlib.pylab as pl

with open("out.txt", "r") as datafile:
    json_data = datafile.read().replace('\n', '')

dict_data = json.loads(json_data)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(dict_data)
result = json_normalize(dict_data['series'], 'pointlist')
result.columns = ['time', 'events per second']

result['time'] -= result['time'][0]
result['time'] *= 0.001
result['events per second'] *= 500000

#pl.figure()
#seaborn.regplot(x='time', y='messages per second', data=result)
#pl.figure()
#seaborn.tsplot(data=result, value='messages per second', time='time')
pl.figure()
seaborn.tsplot([result['events per second']], time=result.time)

with open("bytes_in.txt", "r") as datafile:
    json_bytes_in = datafile.read().replace('\n', '')

with open("bytes_out.txt", "r") as datafile:
    json_bytes_out = datafile.read().replace('\n', '')

dict_bytes_in = json.loads(json_bytes_in)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dict_bytes_in)
result_bytes_in = json_normalize(dict_bytes_in['series'], 'pointlist')
result_bytes_in.columns = ['time', 'bytes per second']

dict_bytes_out = json.loads(json_bytes_out)
result_bytes_out = json_normalize(dict_bytes_out['series'], 'pointlist')
result_bytes_out.columns = ['time', 'events per second']

result_bytes_out['events per second'] *= 0.000000266
result_bytes_out['events per second'] *= 0.5
result_bytes_out['time'] -= result_bytes_out['time'][0]
result_bytes_out['time'] *= 0.001


pl.figure()
#seaborn.tsplot([result_bytes_in['bytes per second']], time=result_bytes_in.time)
seaborn.tsplot([result_bytes_out['events per second']], time=result_bytes_out.time)#, color='indianred'
# Events per second (x10^6)
# Time (seconds)

pl.figure()
seaborn.regplot(x=result_bytes_out.time, y=result_bytes_out['events per second'])

pl.show()