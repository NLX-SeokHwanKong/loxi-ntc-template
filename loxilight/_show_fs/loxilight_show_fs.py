import textfsm

# cat /proc/uptime; hostnamectl

traceroute = '''
| FILE SYSTEM |   TYPE   | SIZE | USED | AVAIL | USE% |          MOUNTED ON          |
|-------------|----------|------|------|-------|------|------------------------------|
| udev        | devtmpfs | 1.9G |    0 | 1.9G  | 0%   | /dev                         |
| tmpfs       | tmpfs    | 393M | 1.5M | 392M  | 1%   | /run                         |
'''

with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)