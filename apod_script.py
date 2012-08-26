import urllib2
import os
from os.path import basename 
from urlparse import urlsplit 


from BeautifulSoup import BeautifulSoup 
host = "http://apod.nasa.gov/apod"
url = "%s/archivepix.html" %host
count =0

# import pdb; pdb.set_trace()

url_content =urllib2.urlopen(url).read()
soup = BeautifulSoup(url_content)
b_tags = soup.find('b')
link_tags = b_tags.findAll('a')

for link_tag in link_tags:
    
    href_tag = link_tag['href']
    link_url = "%s/%s" % (host,href_tag)
    link_content = urllib2.urlopen(link_url).read()
    link_soup = BeautifulSoup(link_content)
    img_tags = link_soup.find('img')
    if img_tags is  None:
        continue
    img_url = "%s/%s" % (host,img_tags['src'])

    try:
        img_data = urllib2.urlopen(img_url).read()
        with open(str(href_tag) + ".jpg",'wb') as foo:
            foo.write(img_data)
            foo.close()
    except:
        raise

    count=count+1
    print "Gettting image " + str(count) + "|" + str(href_tag)
    if count>50: 
        break