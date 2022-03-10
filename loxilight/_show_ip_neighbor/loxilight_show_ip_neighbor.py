import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
> show ip neighbor all
| VRF | NEXT HOP | SOURCE MAC | DESTINAION MAC | INTERFACE | IS INSTALL | HW INSTALL |
|-----|----------|------------|----------------|-----------|------------|------------|
| 1   | 128.0.0.1| 01:42:b4:fc:af:a9   | 01:42:b4:fc:af:19       | eth1      |            |            |
| 2   | 228.0.0.1| 02:42:b4:fc:af:a9   | 02:42:b4:fc:af:29       | eth2      |            |            |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)