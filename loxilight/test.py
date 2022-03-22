sysinfo = '''
| SYSTEM UPTIME | IDLE UPTIME | STATIC HOSTNAME |  ICON NAME  | CHASSIS |            MACHINE ID            |             BOOT ID              | VRTUALIZATION |         OS         |         KERNEL          | ARCHITECTURE |
|---------------|-------------|-----------------|-------------|---------|----------------------------------|----------------------------------|---------------|--------------------|-------------------------|--------------|
|     106642.18 |  1691164.93 | node1           | computer-vm | vm      | 63ef5212e8974bbea9d4b039e7621b96 | dff08dd413ec4f148f55b251b5824f01 | xn            | Ubuntu 20.04.3 LTS | Linux 5.11.0-38-generic | x86-64       |
'''

nodeinfo = sysinfo.split('\n')[3]
nodeList = nodeinfo.split('|')

sys_uptime = float(nodeList[1])
idle_uptime = float(nodeList[2])

print(sys_uptime)
print(idlet_uptime)
