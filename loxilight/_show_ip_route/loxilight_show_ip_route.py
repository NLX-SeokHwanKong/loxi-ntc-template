import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
 show ip route all
| VRF  |        ROUTE        | IS INSTALL |     NEXTHOP      |     INTERFACE     |
|------|---------------------|------------|------------------|-------------------|
| 2000 |   192.168.10.102/32 | U          |   192.168.10.102 |              hs1  |
| 2000 |      10.41.43.60/32 | I          |      10.233.64.2 |        hsvlan110  |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)