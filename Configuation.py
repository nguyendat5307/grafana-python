from influxdb import InfluxDBClient
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'CONFIGUATION')
client.create_database('CONFIGUATION')
Station = "MIND"
while True:
    print("1 Thêm Tag\n2 Cập nhật Tag")   
    s = input("Chọn: ")
    if s == "1":
        NODE_ID = input("NODE ID: ")
        NODE_NAME = input("NODE NAME: ")
        DEVICE_ID = input("DEVICE ID: " )
        DEVICE_NAME = input("DEVICE NAME: ")
        ADDRESS = input("ADRRESS: ")
        CHANEL = input("CHANEL: ")
        TAG_NAME = input("TAG NAME: ")
        TYPE = input("TAG TYPE: ")
        if TYPE != 'bool':
            k = 'r'
            CHANEL2 = str(int(CHANEL) + 1).zfill(2)
            Register_1 = 'p0v' + DEVICE_ID + k + hex(int(ADDRESS))[2:].zfill(4) + 'x' + CHANEL
            Register_2 = 'p0v' + DEVICE_ID + k + hex(int(ADDRESS)+1)[2:].zfill(4) + 'x' + CHANEL2
        else:
            k = 'c' 
        TAG_CONFIG = [
            {
                "measurement": Station,
                "tags": 
                {
                    "NODE_ID": NODE_ID,
                    "DEVICE_ID": DEVICE_ID,
                    "ADDRESS": ADDRESS
                },
                "fields":
                {
                    "NODE_NAME": NODE_NAME,
                    "DEVICE_NAME": DEVICE_NAME,
                    "TAG_NAME": TAG_NAME,
                    "TYPE": TYPE,
                    "CHANEL": CHANEL,
                    "Register_1": Register_1,
                    "Register_2": Register_2
                }
            }
            ]
        client.write_points(TAG_CONFIG)
    elif s == "2":
        print("Chọn Tag muốn cập nhật: ")
        t = input("Tag: ")
