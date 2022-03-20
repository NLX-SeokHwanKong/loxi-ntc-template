import textfsm

traceroute = '''
| PID | USER | PRIORITY | NICE | VIRTUAL MEMORY | RESIDENT MEMORY | SHARED MEMORY | STATUS | CPU% | MEM% | RUNNING TIME | PROCESS NAME |
|-----|------|----------|------|----------------|-----------------|---------------|--------|------|------|--------------|--------------|
|   1 | root |       20 |    0 |         169184 |           12976 |          8116 | S      |  0.0 |  0.3 | 0:03.15      | systemd      |
|   2 | root |       20 |    0 |              0 |               0 |             0 | S      |  0.0 |  0.0 | 0:00.02      | kthreadd     |
'''

with open('loxilight_show_cpu.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)