import re
with open('/Volumes/Data/Github/Porfolio/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the styling on the first skills icon box which was missing some flex configurations 
# and remove some empty or weird HTML comments
text = text.replace('<!-- <div style="text-align:center; margin-right:20px;">', '')
text = text.replace('</div> -->', '</div>')
text = text.replace('<!-- <div class="col-md-12 mt-4 mt-md-0 icon-box" data-aos="lefade-up" data-aos-delay="100"', '<div class="col-md-12 mt-4 mt-md-0 icon-box" data-aos="fade-up" data-aos-delay="100"')
text = text.replace('style="background:#fff">', 'style="background:#fff">')

# Re-hide the ones the user actually wanted hidden (Machine learning and deep learning) 
# I will just write a proper regex to clean up the commented ones
