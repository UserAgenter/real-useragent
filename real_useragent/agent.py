import os
from random import choice

current = os.path.abspath(os.path.dirname(__file__))

desk_path = os.path.join(current, "desktop_useragent.txt")
mob_path = os.path.join(current, "mobile_useragent.txt")


class UserAgent:
    def __init__(self):
        # Load User-Agent from files
        self.desktop = self._load_useragent(desk_path)
        self.mobile = self._load_useragent(mob_path)

    @staticmethod
    def _load_useragent(path):
        """Loads a list of User-Agent strings from a file."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"File Not Found: {path}")
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]

    def random_useragent(self, mode="desktop", browser=None):
        """
        Receives a User-Agent based on the mode and optional browser filter.
        :param mode: "desktop" OR "mobile"
        :param browser: Filter by browser (ex: "chrome")
        :return: A random User-Agent
        """
        agents = self.desktop if mode == "desktop" else self.mobile

        # Filter by browser if provided
        if browser:
            agents = [ua for ua in agents if browser.lower() in ua.lower()]

        if not agents:
            raise ValueError("\t[ Error ] No Matching User-Agent Found.\t")

        return choice(agents)

    def chrome_useragent(self):
        return self.random_useragent(browser="chrome")

    def firefox_useragent(self):
        return self.random_useragent(browser="firefox")

    def desktop_useragent(self):
        return self.random_useragent(mode="desktop")

    def mobile_useragent(self):
        return self.random_useragent(mode="mobile")

    def safari_useragent(self):
        return self.random_useragent(browser="safari")

    def get_useragent(self, mode="desktop", browser=None):
        return self.random_useragent(mode=mode, browser=browser)

    def mobile_chrome_useragent(self):
        return self.random_useragent(mode="mobile", browser="chrome")

    def desktop_chrome_useragent(self):
        return self.random_useragent(mode="desktop", browser="chrome")

    def mobile_firefox_useragent(self):
        return self.random_useragent(mode="mobile", browser="firefox")

    def desktop_firefox_useragent(self):
        return self.random_useragent(mode="desktop", browser="firefox")

    def mobile_safari_useragent(self):
        return self.random_useragent(mode="mobile", browser="safari")

    def desktop_safari_useragent(self):
        return self.random_useragent(mode="desktop", browser="safari")

    def desktop_linux_useragent(self):
        return self.random_useragent(mode="desktop", browser="linux")

    def desktop_mac_useragent(self):
        return self.random_useragent(mode="desktop", browser="mac")

