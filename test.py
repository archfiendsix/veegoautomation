

import logging
import time
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

print(username)

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s %(message)s',
                    handlers=[logging.StreamHandler()])



# import time

start_time = 1673946151303
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(start_time)))


# current_time = time.time()
# current_timestamp = datetime.fromtimestamp(current_time/1000)
# current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(current_time))
# print(f'Current Time: {datetime.now()}')


# print(current_time)
# diff = current_timestamp - start_time
# print(diff)
d= datetime.now()
# d =  datetime.utcfromtimestamp(time.localtime()) - datetime.utcfromtimestamp(time.localtime())
print(d)
while True:
    x=0
    x+=1
    logging.info(x)
    if x==5:
        break
    elif time.time() - start_time > 4:
        break
    else:
        time.sleep(10)



