from ncclient import manager
from pprint import pprint
from pprint import pformat
import xmltodict
import xml.dom.minidom

router = {
   'host': '10.199.199.250',
   'port': '830',
   'username': 'admin',
   'password': 'cisco'
}

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface>
       <name>GigabitEthernet1</name>
     </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface>
       <name>GigabitEthernet1</name>
     </interface>
  </interfaces-state>
</filter> """


with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], device_params={'name': 'iosxe'}, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
      print('*' * 50)
      print(capability)
    print('*** I AM CONNECTED ***')
    interface_netconf = m.get(netconf_filter)
    print('*** Getting runnung config ***')


interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
# print the dictionary by uncommenting line below
# pprint(interface_python)
intname = str(interface_python['interfaces']['interface']['name'])
# prittyinterface = str(intname)
print(intname)
config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("START")
print(f"NAME: {config['name']}")
print(f"DESCRIPTION: {config['description']}")
print(f"PACKETS in: {op_state['statistics']['in-unicast-pkts']}")
