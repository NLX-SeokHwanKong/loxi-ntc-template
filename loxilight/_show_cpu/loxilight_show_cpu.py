import textfsm

# show device topcpu
traceroute = '''
|  PID   |  USER  | PRIORITY | NICE | VIRTUAL MEMORY | RESIDENT MEMORY | SHARED MEMORY | STATUS | CPU% | MEM% | RUNNING TIME | PROCESS NAME |
|--------|--------|----------|------|----------------|-----------------|---------------|--------|------|------|--------------|--------------|
|   3426 | root   |       20 |    0 |        1309268 |          565180 |         70408 | S      | 13.3 |  3.5 | 128:43.06    | kube-ap+     |
|   2230 | root   |       20 |    0 | 10.3g          |          243164 |        103584 | S      |  6.7 |  1.5 | 57:39.19     | etcd         |
| 454247 | admin2 |       20 |    0 |          12232 |            3800 |          3012 | R      |  6.7 |  0.0 | 0:00.01      | top          |
|      1 | root   |       20 |    0 |         167848 |           11696 |          8360 | S      |  0.0 |  0.1 | 0:05.25      | systemd      |
|      2 | root   |       20 |    0 |              0 |               0 |             0 | S      |  0.0 |  0.0 | 0:00.02      | kthreadd     |
|      3 | root   |        0 |  -20 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | rcu_gp       |
|      4 | root   |        0 |  -20 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | rcu_par+     |
|      6 | root   |        0 |  -20 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | kworker+     |
|      7 | root   |       20 |    0 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:21.59      | kworker+     |
|      9 | root   |        0 |  -20 |              0 |               0 |             0 | I      |  0.0 |  0.0 | 0:00.00      | mm_perc+     |
'''

with open('loxilight_show_cpu.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)