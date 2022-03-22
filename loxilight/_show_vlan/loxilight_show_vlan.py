import textfsm

# show vlan all

traceroute = '''
|   NAME    | VLAN | STATUS |     PORTS     |
|-----------|------|--------|---------------|
| hsvlan110 |  110 | UP     |  hs3 2000(UP) |
|           |      |        |  hs2 2000(UP) |
|           |      |        |               |
'''


with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)