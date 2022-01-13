from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

router = {
   'host': '10.199.199.250',
   'port': '830',
   'username': 'admin',
   'password': 'cisco'
}

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

running_config = m.get_config('running').xml
print(xml.dom.minidom.parseString(running_config).toprettyxml())

m.close_session()