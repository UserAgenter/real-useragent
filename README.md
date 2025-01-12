# Real User Agent Generator


Real User Agent With Auto Sync in Requests Module.


# Installation

```bash
pip install real-useragent
```

# Usage

```python
import requests
import real_useragent

s = requests.Session()
print(s.headers['User-Agent'])

# Without a session
resp = requests.get('https://httpbin.org/user-agent')
print(resp.json()['user-agent'])
```

User Agents are Randomized Per-Session or Per-Request. Individual HTTP requests without a session will each have a random User-Agent selected from the list in [desktop_useragent.txt](https://github.com/UserAgenter/real-useragent/blob/main/real-useragent/desktop_useragent.txt) or [mobile_useragent.txt](https://github.com/UserAgenter/real-useragent/blob/main/real-useragent/mobile_useragent.txt) all files automatically updated every 8 hours.


Programmer : [@Pymmdrza](https://github.com/Pymmdrza)

Credit : [Mmdrza.Com](https://mmdrza.com)

# Donate

Donate with Bitcoin: `1MMDRZA12xdBLD1P5AfEfvEMErp588vmF9`
