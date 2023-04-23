import re
##############################part1
#log_file = "/var/log/syslog"
#log_pattern = r"^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) (\S+) (\S+): (.*)$"
#logs = []
##############################
#with open(log_file, "r") as fr:
#    for line in fr:
#        match = re.match(log_pattern, line)
#        if(match):
#            time_stamp = match.group(1)
#            host_name = match.group(2)
#            program = match.group(3)
#            message = match.group(4)
#            log = {"time_stamp" : time_stamp,
#                     "host_name" : host_name,
#                     "program" : program,
#                     "message" : message}
#            logs.append(log)
#with open("total_log", "w") as fw:
#    for log in logs:
#        fw.write(str(log) + "\n\n")
##############################part2
log_file = "/var/log/syslog"
log_pattern = r"^Apr(\s+\d{1,2}\s+13:\d{2}:\d{2}) (\S+) (\S+): (.*)$"
logs = []
##############################part2
with open(log_file, "r") as fr:
    for line in fr:
        match = re.match(log_pattern, line)
        if(match):
            time_stamp = match.group(1)
            host_name = match.group(2)
            program = match.group(3)
            message = match.group(4)
            log = {"time_stamp" : time_stamp,
                     "host_name" : host_name,
                     "program" : program,
                     "message" : message}
            logs.append(log)
with open("part_log", "w") as fw:
    for log in logs:
        fw.write(str(log) + "\n\n")
