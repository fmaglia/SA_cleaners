#from bs4 import BeautifulSoup
#import urllib

#page3 = urllib.urlopen("http://betane.ws/e1c4").read()
#soup3 = BeautifulSoup(page3,"lxml")

#desc = soup3.findAll(attrs={"name":"description"}) 
#print desc[0]['content'].encode('utf-8')

url = "http://ow.ly/R5YSh"


from mechanize import Browser
from BeautifulSoup import BeautifulSoup

br = Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
r = br.open(url)
soup = BeautifulSoup(r)
print soup.find("title").text
