import os
import sys
import random
import requests.utils
from .agent import UserAgent

__version__ = "1.0.55"

UA_PLATFORM = sys.platform

current_path = os.path.abspath(os.path.dirname(__file__))
desktop_file = os.path.join(current_path, 'desktop_useragent.txt')
mobile_file = os.path.join(current_path, 'mobile_useragent.txt')

with open(desktop_file) as fh:
    desktop_agents = fh.read().splitlines()

with open(mobile_file) as fh:
    mobile_agents = fh.read().splitlines()

requests.utils.default_user_agent = lambda: random.choice(desktop_agents)

if 'android' in UA_PLATFORM.lower():
    requests.utils.default_user_agent = lambda: random.choice(mobile_agents)

if 'ios' in UA_PLATFORM.lower():
    requests.utils.default_user_agent = lambda: random.choice(mobile_agents)
