import re

with open('/Volumes/Data/Github/Porfolio/assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# 5. Make the Skills sections also use the glassmorphism. They were using style="background:#fff" inline, so we need to fix the HTML for that.
