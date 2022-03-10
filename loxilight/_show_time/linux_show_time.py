import textfsm

traceroute = '''
               Local time: Thu 2022-03-10 04:17:09 UTC
           Universal time: Thu 2022-03-10 04:17:09 UTC
                 RTC time: Thu 2022-03-10 04:17:07
                Time zone: Etc/UTC 
System clock synchronized: no
              NTP service: inactive
          RTC in local TZ: no
'''

with open('linux_show_time.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)