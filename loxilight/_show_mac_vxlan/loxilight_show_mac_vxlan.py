import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
|         MAC         | VXLAN | VRF  | DESTINAION IP | VETP ID | STATUS |
|---------------------|-------|------|---------------|---------|--------|
| 5a:64:83:18:29:3e |   100 | 2000 | 0xc0a80a67    | 0x2     | I      |
| c2:51:9b:e9:9f:70 |   100 | 2000 | 0xc0a80a69    | 0x3     | I      |
| 06:02:6a:0a:a8:c0 |   100 | 2000 | 0xc0a80a6a    | 0x5     | I      |
| 06:02:67:0a:a8:c0 |   100 | 2000 | 0xc0a80a67    | 0x2     | I      |
| 06:02:68:0a:a8:c0 |   100 | 2000 | 0xc0a80a68    | 0x4     | I      |
| c6:3e:22:61:94:29 |   100 | 2000 | 0xc0a80a66    | 0x1     | I      |
| 06:02:66:0a:a8:c0 |   100 | 2000 | 0xc0a80a66    | 0x1     | I      |
| d2:c1:c2:1f:f8:c3 |   100 | 2000 | 0xc0a80a68    | 0x4     | I      |
| 92:b8:07:14:cb:bd |   100 | 2000 | 0xc0a80a6a    | 0x5     | I      |
| 06:02:69:0a:a8:c0 |   100 | 2000 | 0xc0a80a69    | 0x3     | I      |

'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)