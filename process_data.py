import json
import time
from kafka import KafkaProducer


BOOTSTRAP_SERVER = '192.168.178.50:9092'
TELEMETRY_FILE = '2018-06-17T133707Z.json'

with open(TELEMETRY_FILE, 'r') as f:
    data = json.load(f)

split_data = {}
for i in data:
    if split_data.get(i['_T']):
        split_data[i['_T']].append(i)
    else:
        split_data[i['_T']] = [i]

print("Pausing for 5 -- start up the dashboard")
time.sleep(5)

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# for i in split_data['LogPlayerPosition']:
#     producer.send('pubg', i)
#     time.sleep(0.1)

for i in data:
    if i['_T'] == 'LogPlayerPosition':
        producer.send('pubg', i)
        time.sleep(0.05)
    elif i['_T'] == 'LogPlayerKill':
        producer.send('pubg-kill-log', i)
        time.sleep(0.05)

producer.close()