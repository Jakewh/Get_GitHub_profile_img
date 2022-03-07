import requests
from bs4 import BeautifulSoup as bs

"""
  ____      _      ____ _ _   _   _       _                        __ _ _      
 / ___| ___| |_   / ___(_) |_| | | |_   _| |__    _ __  _ __ ___  / _(_) | ___ 
| |  _ / _ \ __| | |  _| | __| |_| | | | | '_ \  | '_ \| '__/ _ \| |_| | |/ _ \
| |_| |  __/ |_  | |_| | | |_|  _  | |_| | |_) | | |_) | | | (_) |  _| | |  __/
 \____|\___|\__|  \____|_|\__|_| |_|\__,_|_.__/  | .__/|_|  \___/|_| |_|_|\___|
                                                 |_|                           
 _                 
(_)_ __ ___   __ _ 
| | '_ ` _ \ / _` |
| | | | | | | (_| |
|_|_| |_| |_|\__, |
             |___/ V1
"""

github_user = input("Vložte Github uživatele: ")
url = "https://github.com/" + github_user
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find("img", {"alt" : "Avatar"})["src"]
print(profile_image)