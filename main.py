import re
from bs4 import BeautifulSoup

class HTMLCleaner:
    def __init__(self, html):
        self.html = html

    def clean(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        return str(soup)

def clean_html(html):
    cleaner = HTMLCleaner(html)
    return cleaner.clean()

# Misol:
html = """
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Example</h1>
    <p>This is an example.</p>
    <script>alert('Hello World!');</script>
    <style>body { background-color: #f2f2f2; }</style>
  </body>
</html>
"""

print(clean_html(html))
```

Kodda `HTMLCleaner` klassi yaratilib, unda `clean` metodi yozilgan. Bu metod `BeautifulSoup` kutubxonasidan foydalanib, HTML belgilarini tozalaydi. `script` va `style` elementlari olib tashlanadi. `clean_html` funktsiyasi `HTMLCleaner` klassining `clean` metodi orqali ishlaydi. Misol uchun, HTML belgilarini tozalash uchun misol berilgan.
