import re

# image mappings
img_map = {
    "NK ASSOCIATES": "assets/img/project/nkassosiate.png",
    "primehrms-ios": "assets/img/project/primeHRMS.png",
    "PrismaLedge": "assets/img/project/prismaLedge.png",
    "wind@wi": "assets/img/project/win@wi.png",
    "Service proz": "assets/img/project/Serviceproz.png",
    "green-solution-ios": "assets/img/project/greenSolution.png",
    "Fluently": "assets/img/project/Fluently.png",
    "Breakdown": "assets/img/project/breakDown.png",
    "Bookestan": "assets/img/project/bookestan2.png"
}

with open('/Volumes/Data/Github/Porfolio/index.html', 'r') as f:
    text = f.read()

for name, img in img_map.items():
    encoded_name = name.replace(' ', '+')
    placeholder = f'https://placehold.co/600x400/EAEAEA/333333?text={encoded_name}'
    # The actual structure is:
    # <h4>{name}</h4>
    # </center>
    # <div class="...">
    # <img src="https://placehold.co..."
    # We can just search for the placehold.co link with the encoded name.
    if placeholder in text:
        text = text.replace(placeholder, img)

with open('/Volumes/Data/Github/Porfolio/index.html', 'w') as f:
    f.write(text)

