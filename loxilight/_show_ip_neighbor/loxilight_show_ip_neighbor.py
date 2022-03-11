import textfsm

# cat /proc/uptime; hostnamectl
# ^[|]\s+VRF\s+[|]\s+NEXT HOP\s+[|]\s+SOURCE MAC\s+[|]\s+DESTINAION MAC\s+[|]\s+INTERFACE\s+[|]\s+IS INSTALL\s+[|]\s+HW INSTALL.*$$ -> Next.NoRecord

traceroute = '''
| VRF | NEXT HOP | SOURCE MAC | DESTINAION MAC | INTERFACE | IS INSTALL | HW INSTALL |
|-----|----------|------------|----------------|-----------|------------|------------|
| 1   | 128.0.0.1 | 01:42:b4:fc:af:a9   | 01:42:b4:fc:af:19       | eth1      |    aaa        |     bbb       |
| 2   | 228.0.0.1 | 02:42:b4:fc:af:a9   | 02:42:b4:fc:af:29       | eth2      |     ccc       |    ddd        |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)