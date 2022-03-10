import textfsm

# cat /proc/uptime; hostnamectl

#traceroute = '''
#|   NAME    | VLAN | STATUS |    PORTS   |
#|-----------|------|--------|------------|
#| hsvlan110 |  110 | UP     | eth0, eth1 |
#'''
traceroute = '''
| hsvlan110 |  110 | UP     | eth0, eth1 |
'''

with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)