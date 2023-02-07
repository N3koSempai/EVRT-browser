from bs4 import BeautifulSoup
import requests
import webbrowser
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
headers = {"Accept-Encoding": "gzip"}


res = requests.get("https://es.wikipedia.org/wiki/Wikipedia:Portada", headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
x= soup.prettify()

f = open('index.html', 'w')
f.write(soup.prettify())
f.close()

#webbrowser.open_new_tab('index.html')



class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.secondary_palette = "Orange"
        
        return MDLabel(text="hola que tal", halign="center")
    
    def search(self):
        #res = requests.get("https://es.wikipedia.org/wiki/Wikipedia:Portada", headers=headers)
        pass
MainApp().run()
