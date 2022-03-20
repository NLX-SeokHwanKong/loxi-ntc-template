import textfsm

traceroute = '''
show device date
|         LOCAL TIME         |       UNIVERSAL TIME       |          RTC TIME          |         TIME ZONE          | SYSTEM CLOCK SYNCHRONIZED  |        NTP SERVICE         |      RTC IN LOCAL TZ       |
|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
| 화 2022-03-15 16:37:32 KST | 화 2022-03-15 07:37:32 UTC | 화 2022-03-15 07:37:33     | Asia/Seoul (KST, +0900)    | yes                        | active                     | no                         |
'''

with open('loxilight_show_time.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)