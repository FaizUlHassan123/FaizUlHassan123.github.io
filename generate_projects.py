import re

projects = [
    ("NK ASSOCIATES", "https://apps.apple.com/pk/app/nk-associates/id1511147987"),
    ("primehrms-ios", "https://apps.apple.com/pk/app/primehrms/id1448029069"),
    ("PrismaLedge", "https://apps.apple.com/pk/app/prismaledge/id1450111574"),
    ("wind@wi", "https://apps.apple.com/pk/app/wind-wi/id1569159256"),
    ("Service proz", "https://apps.apple.com/pk/app/service-proz/id616192452"),
    ("green-solution-ios", "https://apps.apple.com/pk/app/green-solution-group/id667938798"),
    ("Fluently", "https://apps.apple.com/pk/app/fluently-find-penpal-tandem/id1415079921"),
    ("Breakdown", "https://apps.apple.com/pk/app/breakdown-inc/id1459289134"),
    ("Mind", "https://apps.apple.com/pk/app/mind-positive-affirmations/id1591557431"),
    ("Bookestan", "https://apps.apple.com/us/app/apple-store/id1548724755"),
    ("Yalla Pay", "https://apps.apple.com/pk/app/yalla-pay/id1606733407"),
    ("HairstyleGlam", "https://apps.apple.com/us/app/hairstyleglam/id1434908616"),
    ("Forever Live", "https://apps.apple.com/pk/app/foreverlive-app/id6443921210"),
    ("Dropchats", "https://apps.apple.com/pk/app/dropchats/id6443835631"),
    ("NOW", "https://itunes.apple.com/us/app/Now/id1459527321?ls=1&mt=8"),
    ("MyGoalPal", "https://apps.apple.com/us/app/my-goalpal/id1506651949"),
    ("DogBlog", "https://apps.apple.com/us/app/dogblog/id6473627469"),
    ("NightLite", "https://apps.apple.com/us/app/tourstream/id1619341393"),
    ("Tour Cast", "https://apps.apple.com/us/app/tourstream/id1619341393"),
    ("The Collective", "https://apps.apple.com/pk/app/artemis-collective/id1642523150"),
    ("TruckSpot", "https://apps.apple.com/pk/app/truckspot/id1217463622"),
    ("StreAds", "#")
]

html_blocks = []
for name, link in projects:
    encoded_name = name.replace(' ', '+')
    block = f"""        <div class="col-lg-4 col-md-6 portfolio-item filter-app">
          <center>
            <h4>{name}</h4>
          </center>
          <div class="portfolio-wrap" style="height: 250px; display: flex; align-items: center; justify-content: center; background-color: #f8f9fa;">
            <img src="https://placehold.co/600x400/EAEAEA/333333?text={encoded_name}" class="img-fluid" alt="{name}" style="object-fit: cover; width: 100%; height: 100%;">
            <div class="portfolio-info">
              <div class="portfolio-links">
                <a href="{link}" target="_blank" title="App Store Link"><i class="bx bxl-apple"></i></a>"""
    if name == "Breakdown":
         block += f"""\n                <a href="https://play.google.com/store/apps/details?id=com.crinoid.breakdown" target="_blank" title="Play Store Link"><i class="bx bxl-play-store"></i></a>"""
    block += f"""
              </div>
            </div>
          </div>
        </div>"""
    html_blocks.append(block)

new_content = '      <div class="row portfolio-container">\n\n' + '\n\n'.join(html_blocks) + '\n\n      </div>'

with open('/Volumes/Data/Github/Porfolio/index.html', 'r') as f:
    text = f.read()

import re

# Replace the specific portfolio container with id "portfolio"
pattern = re.compile(r'      <div class="row portfolio-container">.*?      </div>\n    </div>\n  </section>', re.DOTALL)

res = pattern.sub(new_content + '\n    </div>\n  </section>', text)

with open('/Volumes/Data/Github/Porfolio/index.html', 'w') as f:
    f.write(res)

print("Done")
