# This file tests connection.
from ncclient import manager

m = manager.connect(host='10.199.199.250', port='830', username='admin',
                    password='cisco', device_params={'name':'iosxe'}, hostkey_verify=False)

print(m.connected)