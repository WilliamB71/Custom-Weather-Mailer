import requests
import tempfile
import os

class Image:
    def update():
        response = requests.get("https://camstills.cdn-surfline.com/uk-bournemouth/latest_full.jpg")
        
        with tempfile.beachimage(delete=False) as f:
            f.write(response.content)
            temp_file_name = f.name 