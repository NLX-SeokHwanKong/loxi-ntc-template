import textfsm

# show device topmem
traceroute = '''
| PID  | USER | PRIORITY | NICE | VIRTUAL MEMORY | RESIDENT MEMORY | SHARED MEMORY | STATUS | CPU% | MEM% | RUNNING TIME | PROCESS NAME |
|------|------|----------|------|----------------|-----------------|---------------|--------|------|------|--------------|--------------|
| 3426 | root |       20 |    0 |        1309268 |          565180 |         70408 | S      |  6.2 |  3.5 | 129:00.70    | kube-ap+     |
| 2230 | root |       20 |    0 | 10.3g          |          243164 |        103584 | S      |  0.0 |  1.5 | 57:47.17     | etcd         |
| 3439 | root |       20 |    0 |         819956 |          117532 |         60348 | S      |  0.0 |  0.7 | 37:55.22     | kube-co+     |
| 1610 | root |       20 |    0 |        2899912 |          111596 |         70752 | S      |  6.2 |  0.7 | 56:21.34     | kubelet      |
| 1377 | root |       20 |    0 |        2790140 |           97424 |         53236 | S      |  0.0 |  0.6 | 27:56.89     | dockerd      |
|  479 | root |       19 |   -1 |         166280 |           77580 |         76200 | S      |  0.0 |  0.5 | 1:19.03      | systemd+     |
| 1172 | root |       20 |    0 |        2459224 |           55764 |         32232 | S      |  0.0 |  0.3 | 6:17.25      | contain+     |
| 3427 | root |       20 |    0 |         751548 |           55072 |         32272 | S      |  0.0 |  0.3 | 5:09.29      | kube-sc+     |
| 1984 | root |       20 |    0 |        2310500 |           48492 |         32212 | S      |  0.0 |  0.3 | 0:10.86      | docker       |
| 4154 | root |       20 |    0 |         750736 |           42616 |         30032 | S      |  0.0 |  0.3 | 6:07.16      | coredns      |

'''

with open('loxilight_show_mem.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)