import requests
import gzip
import os


def get_user_agents_json(url):
    """download and return user-agents.json"""
    req = requests.get(url)
    if req.status_code == 200:
        print("Started Downloading user-agents.json.gz")
        # save the file with progress bar without tqdm
        with open("user-agents.json.gz", "wb") as f:
            f.write(req.content)

        print("Successfully Downloaded user-agents.json.gz")
        current = os.path.abspath(os.path.dirname(__file__))
        file = "user-agents.json.gz"
        gzip_path = os.path.join(current, file)
        with gzip.open(gzip_path, "rb") as f:
            data = f.read()
            data = data.decode("utf-8")
            with open("user-agents.json", "w") as f:
                f.write(data)
            print("Successfully Unzipped to  user-agents.json")

        os.remove("user-agents.json.gz")
        print("Successfully Deleted user-agents.json.gz")
        return "user-agents.json"
    else:
        return None


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) > 1 and args[1].startswith("https://"):
        _url_gz = args[1]
        # python get_agent.py <url:str>
        file_json = get_user_agents_json(url=_url_gz)
        if file_json:
            print(f"Successfully Downloaded {file_json}")
        else:
            print("Failed to Download user-agents.json.gz")
    else:
        print("Invalid URL")
