import json
import struct
import paho.mqtt.subscribe as subscribe
from influxdb import InfluxDBClient
client_C = InfluxDBClient('localhost', 8086, 'root', 'root', 'CONFIGUATION')
client_C.create_database('CONFIGUATION')
client_D = InfluxDBClient('localhost', 8086, 'root', 'root', 'DATA')
client_D.create_database('DATA')
Station = "MIND"
topics = ["Advantech/00D0C9E5036A/data"]
auth = {"username":"mind", "password":"123"}
hostname = "202.158.245.111"
b = {}
while True:
    data = client_C.query('select * from ' + Station).get_points()
    m = subscribe.simple(topics, transport="tcp", hostname=hostname, port=16766, auth=auth, retained=False, msg_count=6, qos=0)
    for a in m:
        b.update(json.loads(a.payload))
    print(b)
    for i in data:
            try:
                x = hex(b[i['Register_1']])[2:].zfill(4) + hex(b[i['Register_2']])[2:].zfill(4)
                y = struct.unpack('!f', bytes.fromhex(x))[0]
                print(y)
                json_body = [
                {
                    "measurement": Station,
                    "tags": 
                    {
                        "node": i['NODE_NAME'],
                        "device": i['DEVICE_NAME'],
                        "tag": i['TAG_NAME']
                    },
                    "fields": 
                        {
                            "value": y
                        }
                }
                ]
                client_D.write_points(json_body)
            except:
                print('...')
            