import textfsm

# show ip neighbor all

traceroute = '''
| VRF  |     NEXT HOP     |    SOURCE MAC     |  DESTINAION MAC   |    INTERFACE     |  STATUS   | IS INSTALL |
|------|------------------|-------------------|-------------------|------------------|-----------|------------|
| 2000 |   192.168.10.105 | f2:d7:cf:cf:40:72 | f2:d7:cf:e3:7b:f1 |              hs1 | REACHABLE | I          |
| 2000 |   192.168.10.103 | f2:d7:cf:cf:40:72 | f2:d7:cf:c2:f8:6b |              hs1 | REACHABLE | I          |
| 2000 |      11.233.0.70 | de:ad:02:dd:00:6e | 82:da:74:22:24:5e |        hsvlan110 | REACHABLE | NI         |
| 2000 |     10.233.64.54 | de:ad:02:dd:00:6e | d2:5a:75:85:1f:b1 |        hsvlan110 | REACHABLE | I          |
| 2000 |      11.233.0.69 | de:ad:02:dd:00:6e | 6e:c8:63:83:5d:b7 |        hsvlan110 | REACHABLE | NI         |
| 2000 |      11.233.0.66 | de:ad:02:dd:00:6e | 7e:9a:48:ce:3d:15 |        hsvlan110 | REACHABLE | NI         |
| 2000 |      11.233.0.68 | de:ad:02:dd:00:6e | a6:2a:5e:ec:69:dd |        hsvlan110 | REACHABLE | NI         |
| 2000 |      10.233.64.2 | de:ad:02:dd:00:6e | ea:18:79:0a:54:1d |        hsvlan110 | REACHABLE | I          |
| 2000 |   192.168.10.104 | f2:d7:cf:cf:40:72 | f2:d7:cf:58:c3:b6 |              hs1 | REACHABLE | I          |
| 2000 |   192.168.10.102 | f2:d7:cf:cf:40:72 | f2:d7:cf:56:93:7e |              hs1 | REACHABLE | I          |
| 2000 |   192.168.10.106 | f2:d7:cf:cf:40:72 | f2:d7:cf:3f:83:14 |              hs1 | REACHABLE | I          |
| 2000 |      11.233.0.67 | de:ad:02:dd:00:6e | d2:d2:f5:3a:75:0a |        hsvlan110 | REACHABLE | NI         |
| 2000 |     192.168.10.1 | f2:d7:cf:cf:40:72 | 04:26:02:21:03:07 |              hs1 | REACHABLE | I          |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)