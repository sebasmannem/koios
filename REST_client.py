# Found on http://rest.elkstein.org/2008/02/using-rest-in-python.html

#GET
import urllib2

url = 'http://www.acme.com/products/3322'
response = urllib2.urlopen(url).read()

#POST
import urllib
import urllib2

url = 'http://www.acme.com/users/details'
params = urllib.urlencode({
  'firstName': 'John',
  'lastName': 'Doe'
})
response = urllib2.urlopen(url, params).read()

