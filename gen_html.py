#!/usr/bin/env python3

import os
import json
from subprocess import call

try:
    os.remove('wangjoa.json')
except:
    pass
call(['scrapy', 'crawl', '-o', 'wangjoa.json', 'wangjoa'])

with open('wangjoa.json', 'r') as f:
    post_list = json.loads(f.read())

post_list = sorted(post_list, key=lambda post: (post['name'], post['date']))

post_html_list = [''.join([
    '<div class="post">\n',
    '<div class="title">\n',
    '<span class="name"><a href="{0}">{1}</a></span> / <span class="location">{2}</span><span class="date">{3}</span>\n'.format(post['url'], post['name'], post['location_detail'], post['date']),
    '</div>\n',            
    '<span class="excerpt">{0}</span>\n'.format(post['excerpt']),
    '</div>\n']) for post in post_list]

content = ''.join(post_html_list)

with open('template.html', 'r') as f:
    html = f.read()

html = html.replace('{{content}}', content)

with open('../index.html', 'w') as f:
    f.write(html)

