########################################
import requests
import time
import sys
########################################
url = "https://www.apple.com"     
#number of times to check the url
num_checks = 10
#period between checks
check_interval = 60
########################################
for i in range(num_checks):
    try:
        response = requests.get(url)
        if(response.status_code == 200):
            print(f'{url} is up and running!')
        else:
            print(f'WARNING: {url} returned status code {response.status_code}')
    except request.exceptions.RequestException as e:
        print(f'ERROR: {url} is down or unreachable. Error message: {str(e)}')
    finally:
        time.sleep(check_interval)
########################################
sys.exit(1)
