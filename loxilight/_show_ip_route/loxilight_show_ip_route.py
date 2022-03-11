import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
| HOST-IP    | FLAGS | VRF | NEXTHOP   | IS INSTALL | HW INSTALL | INTERFACE |
|------------|-------|-----|-----------|------------|------------|-----------|
| 128.0.0.1  | flag  | def | 129.0.0.1 | aaa        |    aaa     | eth1      |
| 228.0.0.1  | flag  | def | 229.0.0.1 | bbb        |    bbb     | eth2      |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)