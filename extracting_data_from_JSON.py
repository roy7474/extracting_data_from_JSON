'''Write a program similar to:

import json

data = 
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

---------------------------------------------   
the program:
1) Will prompt for a URL, 
2) read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
3) compute the sum of the numbers in the file and enter the sum below:

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)

Data Format:

The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

    '''
import json
import urllib.request

url = input('Enter location:')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json' 

data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)

print('Retrieving', url)
print('Retrieved', len(data), 'characters')
comment_count = 0

for comment in info['comments']:
    comment_count += comment['count']

print('Count:', len(info['comments']))
print('Sum:', comment_count)