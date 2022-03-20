import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
|         MAC         | VLAN | VRF  | INTERFACE | STATUS |
|---------------------|------|------|-----------|--------|
| 0xd6:95:6c:b7:92:1a |  110 | 2000 | hs3       | I      |
| 0x7a:6b:cc:ee:1c:f2 |  110 | 2000 | hs2       | I      |
| 0xf2:d7:cf:58:c3:b6 | 3801 | 2000 | hs1       | I      |
| 0xf2:d7:cf:e3:7b:f1 | 3801 | 2000 | hs1       | I      |
| 0x04:26:02:21:03:07 | 3801 | 2000 | hs1       | I      |
| 0xf2:d7:cf:3f:83:14 | 3801 | 2000 | hs1       | I      |
| 0xf2:d7:cf:c2:f8:6b | 3801 | 2000 | hs1       | I      |
| 0xf2:d7:cf:56:93:7e | 3801 | 2000 | hs1       | I      |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)