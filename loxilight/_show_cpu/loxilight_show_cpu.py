import textfsm

# show device topcpu
traceroute = '''
| PID  |  USER  | PRIORITY | NICE | VIRTUAL MEMORY | RESIDENT MEMORY | SHARED MEMORY | STATUS | CPU% | MEM% | RUNNING TIME | PROCESS NAME |
|------|--------|----------|------|----------------|-----------------|---------------|--------|------|------|--------------|--------------|
| 1727 | root   |       20 |    0 |        2750656 |          100304 |         67760 | S      |  6.7 |  0.6 | 0:04.71      | kubelet      |
| 4870 | netlox |       20 |    0 |          12208 |            4064 |          3268 | R      |  6.7 |  0.0 | 0:00.01      | top          |
|    1 | root   |       20 |    0 |         167668 |           11436 |          8288 | S      |  0.0 |  0.1 | 0:01.77      | systemd      |
|    2 | root   |       20 |    0 |              0 |               0 |             0 | S      |  0.0 |  0.0 | 0:00.00      | kthreadd     |
|    3 | root   |        0 |  -20 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | rcu_gp       |
|    4 | root   |        0 |  -20 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | rcu_par+     |
|    5 | root   |       20 |    0 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | kworker+     |
|    6 | root   |        0 |  -20 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | kworker+     |
|    7 | root   |       20 |    0 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | kworker+     |
|    8 | root   |       20 |    0 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.05      | kworker+     |
'''

with open('loxilight_show_cpu.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)