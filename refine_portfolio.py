import re

with open('/Volumes/Data/Github/Porfolio/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix typo in meta description
text = text.replace('<meta content="" name="descriptison">', '<meta content="Faiz Ul Hassan Portfolio" name="description">')

# 2. Correct capitalization
text = text.replace('assets/files/SoftWare Engineer iOS Faiz Ul Hassan.pdf', 'assets/files/Software Engineer iOS Faiz Ul Hassan.pdf')

# 3. Clean up the style attributes in About Me tags
text = text.replace('style="<!-- margin-top: 50px;-->"', '')
text = text.replace('style="<!-- border-radius: 50%; -->"', '')

# 4. Remove commented out blocks taking up space
text = re.sub(r'<!--\s+<p>I have worked in diverse fields.*?</div> -->', '', text, flags=re.DOTALL)
text = re.sub(r'<!--\s+<div class="portfolio">.*?</div> -->', '', text, flags=re.DOTALL)
text = re.sub(r'<!--\s+<section id="education" class="services">.*?</div>\n\n  </section> -->', '', text, flags=re.DOTALL)
text = re.sub(r'<!--\s+<div class="col-md-12 mt-4 mt-md-0 icon-box".*?</div> -->', '', text, flags=re.DOTALL)
text = re.sub(r'<!-- contact -->\n        <!-- <div class="col-md-6 mt-4 d-flex align-items-stretch" style="height: 130px;">.*?</div> -->', '', text, flags=re.DOTALL)

with open('/Volumes/Data/Github/Porfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
