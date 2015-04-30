import sys
import urllib2, json
import base64

baseUrl = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
contentBasePath = sys.argv[4]
outputMapFile = sys.argv[5]

QB_PATH = '/bin/querybuilder.json?p.hits=full&p.limit=-1&path=' + contentBasePath + '&property=sling%3avanityPath&property.operation=like&property.value=%25&type=cq%3aPageContent'
url =  baseUrl + QB_PATH

base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request = urllib2.Request(url)

request.add_header("Authorization", "Basic %s" % base64string)

result = urllib2.urlopen(request)
data = json.load(result)

f = open(outputMapFile, 'w')

for hit in data['hits']:
   line = hit['sling:vanityPath'] + ' ' + hit['jcr:path'].replace('/jcr:content','.html')
   print line
   f.write(line + '\n')

f.close()