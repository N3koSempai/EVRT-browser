
from bs4 import BeautifulSoup
import requests
import webbrowser
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
#webbrowser.open_new_tab('index.html')



class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.secondary_palette = "Orange"
        
        return Builder.load_file('./evrt.kv')
    
    def search(self):
        headers = {"Accept-Encoding": "gzip"}
        res = requests.get("https://es.wikipedia.org/wiki/Wikipedia:Portada", headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        x= soup.prettify()
        pass
        f = open('index.html', 'w')
        f.write(soup.prettify())
        f.close()
MainApp().run()

