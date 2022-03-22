import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
|        MAC        | VLAN | VRF  | INTERFACE | STATUS |
|-------------------|------|------|-----------|--------|
| d2:5a:75:85:1f:b1 |  110 | 2000 | hs3       | I      |
| f2:d7:cf:58:c3:b6 | 3801 | 2000 | hs1       | I      |
| ea:18:79:0a:54:1d |  110 | 2000 | hs2       | I      |
| f2:d7:cf:e3:7b:f1 | 3801 | 2000 | hs1       | I      |
| 04:26:02:21:03:07 | 3801 | 2000 | hs1       | I      |
| f2:d7:cf:3f:83:14 | 3801 | 2000 | hs1       | I      |
| f2:d7:cf:c2:f8:6b | 3801 | 2000 | hs1       | I      |
| f2:d7:cf:56:93:7e | 3801 | 2000 | hs1       | I      |
|        MAC        | VXLAN | VRF  | DESTINAION IP  | VETP ID | STATUS |
|-------------------|-------|------|----------------|---------|--------|
| 06:02:6a:0a:a8:c0 |   100 | 2000 | 192.168.10.106 | 0x9     | I      |
| 06:02:67:0a:a8:c0 |   100 | 2000 | 192.168.10.103 | 0x8     | I      |
| 06:02:68:0a:a8:c0 |   100 | 2000 | 192.168.10.104 | 0x7     | I      |
| 6e:c8:63:83:5d:b7 |   100 | 2000 | 192.168.10.106 | 0x9     | I      |
| d2:d2:f5:3a:75:0a |   100 | 2000 | 192.168.10.103 | 0x8     | I      |
| 06:02:66:0a:a8:c0 |   100 | 2000 | 192.168.10.102 | 0x6     | I      |
| a6:2a:5e:ec:69:dd |   100 | 2000 | 192.168.10.105 | 0xa     | I      |
| 82:da:74:22:24:5e |   100 | 2000 | 192.168.10.104 | 0x7     | I      |
| 06:02:69:0a:a8:c0 |   100 | 2000 | 192.168.10.105 | 0xa     | I      |

'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)