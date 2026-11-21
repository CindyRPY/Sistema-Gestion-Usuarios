import urllib.request
import urllib.error
import json
from Api.config import BASE_URL, TIMEOUT

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        try:
            req = urllib.request.Request(url,headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                data = response.read().decode("utf-8")
                return json.loads(data)
        except urllib.error.HTTPError as e:
            print(f"HTTP Error {e.code}: {e.reason}")
        except urllib.error.URLError as e:
            print(f"URL Error: {e.reason}")
        return {}