import json
import os

rd, gr, r = '\x1b[31m', '\x1b[32m', '\x1b[0m'


class dumper:
    def __init__(self):
        self.data = None
        self.desktop = []
        self.mobile = []

    def get_dump(self):
        current = os.path.abspath(os.path.dirname(__file__))
        file = "user-agents.json"
        json_path = os.path.join(current, file)
        with open(json_path) as f:
            _data = json.load(f)
        return _data

    def map_data(self, data):
        for _item in data:
            device = _item['deviceCategory']
            if device == 'mobile':
                useragent = _item['userAgent']
                if useragent in self.mobile:
                    continue
                self.mobile.append(useragent)
            elif device == 'desktop':
                useragent = _item['userAgent']
                if useragent in self.desktop:
                    continue
                self.desktop.append(useragent)
        return

    def update_agents(self):
        self.data = self.get_dump()
        self.map_data(self.data)
        return


dum = dumper()
dum.update_agents()
mobile = dum.mobile
desktop = dum.desktop

# save to file
desktop_file = "desktop_useragent.txt"
mobile_file = "mobile_useragent.txt"
with open(desktop_file, "w") as f:
    for i in desktop:
        f.write(f"{i.strip()}\n")
with open(mobile_file, "w") as f:
    for i in mobile:
        f.write(f"{i.strip()}\n")

os.remove("user-agents.json")
print(f"{gr}Successfully Created New File with Updated User Agents{r} +{rd} Deleted User Agents File{r}")
