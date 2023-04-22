import re
##############################
log_file = "/var/log/syslog"
log_pattern = r"^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) (\S+) (\S+): (.*)$"
##############################
with open(log_file, "r") as f:
    for line in f:
        match = re.match(log_pattern, line)
        if(match):
            time_stamp = match.group(1)
            host_name = match.group(2)
            program = match.group(3)
            message = match.group(4)
            data = {"time_stamp" : time_stamp,
                     "host_name" : host_name,
                     "program" : program,
                     "message" : message}
            print(data)
