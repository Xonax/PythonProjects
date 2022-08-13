import json
import string
import random
from time import *

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

domains = ["yahoo", "gmail", "outlook", "hotmail"]
ends = ["com", "gov", "org", "co"]
names = json.loads(open('names.json').read())

for name in names:
    domain = ''.join(random.choice(domains))
    end = ''.join(random.choice(ends))
    number = random.randrange(6,12)
    username = name.lower() + '@' + domain + '.' + end
    password = ''.join(random.choice(chars) for i in range(number))
    
    sleep(0.2)
    print('username: %s Pass: %s' % (username, password))