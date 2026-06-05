with open('/Volumes/Data/Github/Porfolio/index.html', 'r') as f:
    text = f.read()

img_map = {
    "Yalla Pay": "assets/img/project/YallaPay.png",
    "Dropchats": "assets/img/project/Dropchat.png"
}

for name, img in img_map.items():
    encoded_name = name.replace(' ', '+')
    placeholder = f'https://placehold.co/600x400/EAEAEA/333333?text={encoded_name}'
    text = text.replace(placeholder, img)

with open('/Volumes/Data/Github/Porfolio/index.html', 'w') as f:
    f.write(text)

