# Real User Agent Generator


Real User Agent With Auto Sync in Requests Module.


## Installation

```bash
pip install real-useragent
```

## Usage

Random User Agent on Any Device with any Browser Type (Recommended)

```python
import requests
import real_useragent

s = requests.Session()
print(s.headers['User-Agent'])

# Without a session
resp = requests.get('https://httpbin.org/user-agent')
print(resp.json()['user-agent'])
```

- UserAgent

```python
from real_useragent import UserAgent
ua = UserAgent()
random_useragent = ua.random_useragent()
```

### Random User Agent from Browser Name:

```python
from real_useragent import UserAgent
ua = UserAgent()
chrome_useragent = ua.chrome_useragent()
firefox_useragent = ua.firefox_useragent()
desktop_useragent = ua.desktop_useragent()
mobile_useragent = ua.mobile_useragent()
safari_useragent = ua.safari_useragent()
```

### Random User Agent from Device Type and Browser :

```python
from real_useragent import UserAgent
ua = UserAgent()
mobile_firefox_ua = ua.get_useragent(mode="mobile", browser="firefox")
desktop_chrome_ua = ua.get_useragent(mode="desktop", browser="chrome")
```
### Random User Agent for Device Type (`mode`)

```python
from real_useragent import UserAgent
ua = UserAgent()
# mode : [desktop or mobile]
desktop_useragent = ua.get_useragent(mode="desktop")
mobile_useragent = ua.get_useragent(mode="mobile")
```
- Desktop

```python
from real_useragent import UserAgent
ua = UserAgent()
desktop_firefox_useragent = ua.desktop_firefox_useragent()
desktop_chrome_useragent = ua.desktop_chrome_useragent()
desktop_linux_useragent = ua.desktop_linux_useragent()
desktop_mac_useragent = ua.desktop_mac_useragent()
```

- Mobile :

```python
from real_useragent import UserAgent
ua = UserAgent()
mobile_chrome_useragent = ua.mobile_chrome_useragent()
mobile_firefox_useragent = ua.mobile_firefox_useragent()
mobile_safari_useragent = ua.mobile_safari_useragent()
```


User Agents are Randomized Per-Session or Per-Request. Individual HTTP requests without a session will each have a random User-Agent selected from the list in [desktop_useragent.txt](https://github.com/UserAgenter/real-useragent/blob/main/real-useragent/desktop_useragent.txt) or [mobile_useragent.txt](https://github.com/UserAgenter/real-useragent/blob/main/real-useragent/mobile_useragent.txt) all files automatically updated every 8 hours.


---

Programmer : [@Pymmdrza](https://github.com/Pymmdrza)

Credit : [Mmdrza.Com](https://mmdrza.com)

Medium : [MMDRZA](https://mdrza.medium.com 'medium page mmdrza')

---

# Donate

Donate with Bitcoin: `1MMDRZA12xdBLD1P5AfEfvEMErp588vmF9`


