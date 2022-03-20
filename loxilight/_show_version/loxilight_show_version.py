import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
show device info
| SYSTEM UPTIME | IDLE UPTIME | STATIC HOSTNAME |  ICON NAME  | CHASSIS |            MACHINE ID            |             BOOT ID              | VIRTUALIZATION |         OS         |         KERNEL          | ARCHITECTURE |
|---------------|-------------|-----------------|-------------|---------|----------------------------------|----------------------------------|----------------|--------------------|-------------------------|--------------|
|      95589.79 |  1506411.38 | node1           | computer-vm | vm      | 63ef5212e8974bbea9d4b039e7621b96 | af8ef8583d584137bde9690ad11e8f5b | xen            | Ubuntu 20.04.3 LTS | Linux 5.11.0-38-generic | x86-64       |
'''

with open('loxilight_show_version.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)