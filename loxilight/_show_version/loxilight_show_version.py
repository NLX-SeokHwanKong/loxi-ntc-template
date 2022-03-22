import textfsm

# show device info
traceroute = '''
| SYSTEM UPTIME | IDLE UPTIME | STATIC HOSTNAME |  ICON NAME  | CHASSIS |            MACHINE ID            |             BOOT ID              | VIRTUALIZATION |         OS         |         KERNEL          | ARCHITECTURE |
|---------------|-------------|-----------------|-------------|---------|----------------------------------|----------------------------------|----------------|--------------------|-------------------------|--------------|
|     102872.85 |  1631413.25 | node1           | computer-vm | vm      | 63ef5212e8974bbea9d4b039e7621b96 | dff08dd413ec4f148f55b251b5824f01 | xen            | Ubuntu 20.04.3 LTS | Linux 5.11.0-38-generic | x86-64       |
'''

with open('loxilight_show_version.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)