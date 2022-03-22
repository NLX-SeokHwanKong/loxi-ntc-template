import textfsm

# show device date
traceroute = '''
|         LOCAL TIME          |       UNIVERSAL TIME        |          RTC TIME           |          TIME ZONE          |  SYSTEM CLOCK SYNCHRONIZED  |         NTP SERVICE         |       RTC IN LOCAL TZ       |
|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Tue 2022-03-22 15:38:20 KST | Tue 2022-03-22 06:38:20 UTC | Tue 2022-03-22 06:38:20     | Asia/Seoul (KST, +0900)     | yes                         | active                      | no                          |

'''

with open('loxilight_show_time.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)