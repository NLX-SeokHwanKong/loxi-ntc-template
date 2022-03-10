import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
2969.02 47189.82
   Static hostname: node1
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 63ef5212e8974bbea9d4b039e7621b96
           Boot ID: 7493939962f94cd09258f63d9b5503ba
    Virtualization: xen
  Operating System: Ubuntu 20.04.3 LTS
            Kernel: Linux 5.11.0-38-generic
      Architecture: x86-64
'''

with open('linux_show_version.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)