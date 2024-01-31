# extracting the title from website...

import re
from urllib import request

# sites = ['https://www.google.com', 'https://www.github.com']
sites = ['https://www.google.com']

for s in sites:
    print('Serching....',s)
    u = request.urlopen(s)
    text = u.read()
    # print(str(text))
    title = re.findall('<title>.*</title>', str(text), re.IGNORECASE)  # I --> IGNORECASE
    print(title[0])
