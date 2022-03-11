import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
FDB Table
|      MAC          |  VLAN |   VRF   | INTERFACE | STATUS |
|-------------------|-------|---------|---------- |--------|
| 33:33:00:00:00:01 | 100   | default |   eth0    |   UP   |
| 44:44:00:00:00:01 | 200   | default |   eth1    |   UP   |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)