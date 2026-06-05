import re

with open('/Volumes/Data/Github/Porfolio/assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Glassmorphism for Services / Experience / Skills blocks
# Find the .services .icon-box background and change to rgba + backdrop
text = re.sub(
    r'.services \.icon-box {\s*text-align: center;\s*background: #09203a;',
    '.services .icon-box {\n  text-align: center;\n  background: rgba(9, 32, 58, 0.7);\n  backdrop-filter: blur(10px);\n  border: 1px solid rgba(255, 255, 255, 0.1);',
    text
)

# Also update the bg reference on hover to maintain the effect
text = re.sub(
    r'.services \.icon-box:hover {\s*background: #042e5f;',
    '.services .icon-box:hover {\n  background: rgba(4, 46, 95, 0.85);',
    text
)

# 2. Glowing drop shadow for header links
text = re.sub(
    r'#header \.social-links a:hover {\s*background: #1c7d32;\s*}',
    '#header .social-links a:hover {\n  background: #1c7d32;\n  box-shadow: 0 0 15px rgba(28, 125, 50, 0.7);\n}',
    text
)

text = re.sub(
    r'\.nav-menu a:hover, \.nav-menu \.active > a, \.nav-menu li:hover > a {\s*color: #12d640;\s*text-decoration: none;\s*}',
    '.nav-menu a:hover, .nav-menu .active > a, .nav-menu li:hover > a {\n  color: #12d640;\n  text-shadow: 0 0 10px rgba(18, 214, 64, 0.5);\n  text-decoration: none;\n}',
    text
)

# 3. Add a lift effect to the individual icons inside the Skills tags. 
# They use img tags inside .skills_one divs. We will add a CSS rule for them.
# The previous code had style="text-align:center; margin-right:20px;" for the grid items.
text += """

/* Modern Skill Icon Interactions */
.skills_one > div {
  transition: all 0.3s ease;
  padding: 10px;
  border-radius: 10px;
}

.skills_one > div:hover {
  transform: translateY(-8px);
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 20px rgba(0,0,0,0.3);
}
"""

# 4. Add subtle scale to portfolio images on hover
text = re.sub(
    r'\.portfolio \.portfolio-wrap {\s*transition: 0.3s;',
    '.portfolio .portfolio-wrap {\n  transition: 0.3s;\n  border-radius: 8px;', # While we are at it, slight rounding on portfolio items is modern
    text
)

# Find the img inside wrap to add transition
text += """
.portfolio .portfolio-wrap img {
  transition: transform 0.5s ease;
}

.portfolio .portfolio-wrap:hover img {
  transform: scale(1.1);
}
"""


with open('/Volumes/Data/Github/Porfolio/assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

