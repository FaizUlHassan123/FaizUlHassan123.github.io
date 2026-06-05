with open('/Volumes/Data/Github/Porfolio/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the white backgrounds on the Skills boxes which break the glassmorphism
text = text.replace('style="background:#fff"', '')

# The text for Languages and Databases was dark to match the #fff, make it white now
text = text.replace('<h4 style="text-align:left;color:#09203a">', '<h4 style="text-align:left;color:#fff">')

with open('/Volumes/Data/Github/Porfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
