import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
| VRF  |     NEXT HOP     |    SOURCE MAC     |  DESTINAION MAC   |    INTERFACE     |  STATUS   | IS INSTALL |
|------|------------------|-------------------|-------------------|------------------|-----------|------------|
| 2000 |   192.168.10.105 | f2:d7:cf:cf:40:72 | f2:d7:cf:e3:7b:f1 |              hs1 | REACHABLE | I          |
| 2000 |   192.168.10.103 | f2:d7:cf:cf:40:72 | f2:d7:cf:c2:f8:6b |              hs1 | REACHABLE | I          |
| 2000 |      11.233.0.70 | f6:c3:66:d5:eb:05 | d2:c1:c2:1f:f8:c3 |       hsvxlan100 | REACHABLE | I          |
| 2000 |      11.233.0.69 | f6:c3:66:d5:eb:05 | 92:b8:07:14:cb:bd |       hsvxlan100 | REACHABLE | I          |

'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)