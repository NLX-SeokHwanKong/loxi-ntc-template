import textfsm

# cat /proc/uptime; hostnamectl
#| VRF | NEXT HOP | SOURCE MAC | DESTINAION MAC | INTERFACE | IS INSTALL | HW INSTALL |
#|-----|----------|------------|----------------|-----------|------------|------------|

traceroute = '''
| 1   | 128.0.0.1 | 01:42:b4:fc:af:a9   | 01:42:b4:fc:af:19       | eth1      |    aaa        |     bbb       |
| 2   | 228.0.0.1 | 02:42:b4:fc:af:a9   | 02:42:b4:fc:af:29       | eth2      |     ccc       |    ddd        |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)