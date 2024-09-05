import requests, random, base64
from bs4 import BeautifulSoup
from datetime import datetime

class Search:
    def __init__(self, user_agents_file="user-agents.txt"):
        self.user_agents = self.load_user_agents(user_agents_file)
        self.banned_patterns = [ # Banned patterns in URL results
            'https://support.google.com/legal/answer/',
            'https://accounts.google.com/ServiceLogin%3Fcontinue',
            'https://maps.google.com/maps%3F',
            'https://support.google.com/websearch%3F'
        ]
    
    def load_user_agents(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read().splitlines()
        except Exception as e:
            return [
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
                "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4"
            ]
            
    def generate_cookie(self):
        """Generate a base64 encoded cookie."""
        raw_cookie = f"\b\x01\x12\x1C\b\x01\x12\x12gws_{datetime.today().strftime('%Y%m%d')}-0_RC3\x1A\x02en \x01\x1A\x06\b\x80º¦±\x06"
        return base64.b64encode(raw_cookie.encode()).decode().replace("\n", "")

    def search(self, query):
        """Perform a Google search and return the results."""
        results = []
        page = 0
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": random.choice(self.user_agents),
            "Cookie": f"SOCS={self.generate_cookie()}",
        }      
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            return []
        
        print(f"\033[1;35mSearching for {query}:\033[0m")
        
        soup = BeautifulSoup(response.text, 'html.parser')  
        for link in soup.find_all("a"):
            href = link.get("href")
            identifier = "/url?esrc=s&q=&rct=j&sa=U&url="
            if href and identifier in href:
                url = href.split(identifier)[1]
                if url.startswith("http") or url.startswith("https"):
                    if not any(pattern in url for pattern in self.banned_patterns) and not url in results:
                        results.append(url)

        return results
