
from bs4 import BeautifulSoup
import requests

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
#webbrowser.open_new_tab('index.html')
from webview import WebView


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.secondary_palette = "Orange"
        self.browser = None
        return Builder.load_file('./evrt.kv')
    
    def search(MDScreen):
        headers = {"Accept-Encoding": "gzip"}
        res = requests.get("https://es.wikipedia.org/wiki/Wikipedia:Portada", headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        x= soup.prettify()
        with  open('index.html', 'w') as f:
            f.write(soup.prettify())
    
MainApp().run()

