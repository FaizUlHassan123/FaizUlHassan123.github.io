import re

with open('/Volumes/Data/Github/Porfolio/assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate the hover effect for contact social links and enhance it
text = re.sub(
    r'\.contact \.info-box \.social-links a:hover {\s*color: #12d640;\s*}',
    '.contact .info-box .social-links a:hover {\n  color: #12d640;\n  text-shadow: 0 0 10px rgba(18, 214, 64, 0.5);\n  transform: scale(1.1);\n}',
    text
)

# And add transform transition if it's missing from the base rule
text = re.sub(
    r'\.contact \.info-box \.social-links a {\s*font-size: 18px;\s*display: inline-block;\s*color: #fff;\s*line-height: 1;\s*margin-right: 12px;\s*transition: 0\.3s;\s*}',
    '.contact .info-box .social-links a {\n  font-size: 18px;\n  display: inline-block;\n  color: #fff;\n  line-height: 1;\n  margin-right: 12px;\n  transition: all 0.3s ease;\n}',
    text
)

with open('/Volumes/Data/Github/Porfolio/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
