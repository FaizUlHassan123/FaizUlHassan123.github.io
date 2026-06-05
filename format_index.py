import re

with open('/Volumes/Data/Github/Porfolio/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix capitalization
text = text.replace('Faiz ul hassan', 'Faiz Ul Hassan')
text = text.replace('qaiser', 'Faiz') 
text = text.replace('Qaiser', 'Faiz')
text = text.replace('assets/img/qysr_2.jpg', 'assets/img/profile.jpg') # Genericizing the image name since qysr is likely leftover from a template or other person
# Fixing any leftover "myemail@gmail.com" from the about section
text = text.replace('myemail@gmail.com', 'faizulhassan550@gmail.com')

# Make sure all the skills are formatted correctly
# The user tried to comment out python and c++ earlier
text = re.sub(r'<!--\s*<div style="text-align:center; margin-right:20px;">\s*<img src="assets/img/project/python.svg" alt="Python3".*?</div>\s*-->', '', text, flags=re.DOTALL)
text = re.sub(r'<!--\s*<div style="text-align:center; margin-right:20px;;">\s*<img src="assets/img/skills/c\+\+.svg" alt="C".*?</div>\s*-->', '', text, flags=re.DOTALL)
text = re.sub(r'<!--\s*<div style="text-align:center; margin-right:20px;">\s*<img src="assets/img/skills/cc.svg" alt="C\+\+".*?</div>\s*-->', '', text, flags=re.DOTALL)
text = re.sub(r'<!--\s*<div style="text-align:center; margin-right:20px;">\s*<img src="assets/img/skills/matlab.svg" alt="MATLAB".*?</div>\s*-->', '', text, flags=re.DOTALL)

with open('/Volumes/Data/Github/Porfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done formatting index.html")
