import re

with open('/Volumes/Data/Github/Porfolio/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure all skills sections the user commented out are properly closed out, 
# because there was some mismatched HTML commenting in the diffs they pasted earlier.
text = re.sub(r'<!--\s*<div class="col-md-12 mt-4 mt-md-0 icon-box"[^>]*>\s*<h4[^>]*>Machine Learning</h4>.*?</div>\s*</div>\s*-->', '', text, flags=re.DOTALL)
text = re.sub(r'<!--\s*<div class="col-md-12 mt-4 mt-md-0 icon-box"[^>]*>\s*<h4[^>]*>Deep Learning Frameworks</h4>.*?</div>\s*</div>\s*-->', '', text, flags=re.DOTALL)

with open('/Volumes/Data/Github/Porfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
