import urllib.request


class Image:
    def update():
        urllib.request.urlretrieve(
            "https://camstills.cdn-surfline.com/uk-bournemouth/latest_full.jpg", "Beach_Image.png")
