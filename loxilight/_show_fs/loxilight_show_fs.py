import textfsm

# show device fs*

traceroute = '''
| FILE SYSTEM |   TYPE   | SIZE | USED | AVAIL | USE% |     MOUNTED ON     |
|-------------|----------|------|------|-------|------|--------------------|
| udev        | devtmpfs | 7.8G |    0 | 7.8G  | 0%   | /dev               |
| tmpfs       | tmpfs    | 1.6G | 2.3M | 1.6G  | 1%   | /run               |
| /dev/xvda1  | ext4     | 49G  | 33G  | 14G   | 71%  | /                  |
| tmpfs       | tmpfs    | 7.8G |    0 | 7.8G  | 0%   | /dev/shm           |
| tmpfs       | tmpfs    | 5.0M |    0 | 5.0M  | 0%   | /run/lock          |
| tmpfs       | tmpfs    | 7.8G |    0 | 7.8G  | 0%   | /sys/fs/cgroup     |
| /dev/loop1  | squashfs | 111M | 111M |     0 | 100% | /snap/core/12821   |
| /dev/loop2  | squashfs | 62M  | 62M  |     0 | 100% | /snap/core20/1376  |
| /dev/loop0  | squashfs | 111M | 111M |     0 | 100% | /snap/core/12725   |
| /dev/loop3  | squashfs | 4.7M | 4.7M |     0 | 100% | /snap/kafkactl/109 |
| /dev/loop4  | squashfs | 68M  | 68M  |     0 | 100% | /snap/lxd/21835    |
| /dev/loop5  | squashfs | 62M  | 62M  |     0 | 100% | /snap/core20/1361  |
| /dev/loop6  | squashfs | 4.7M | 4.7M |     0 | 100% | /snap/kafkactl/107 |
| /dev/loop7  | squashfs | 68M  | 68M  |     0 | 100% | /snap/lxd/22526    |
| tmpfs       | tmpfs    | 1.6G |    0 | 1.6G  | 0%   | /run/user/1000     |
| tmpfs       | tmpfs    | 1.6G |    0 | 1.6G  | 0%   | /run/user/1001     |
| tmpfs       | tmpfs    | 1.6G |    0 | 1.6G  | 0%   | /run/user/1004     |
'''

with open('template.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)