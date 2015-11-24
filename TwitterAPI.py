# -*- coding: utf-8 -*-
# Accessing Twitter API
# Author - Janu Verma
# j.verma5@gmail.com


import oauth2 as oauth
import urllib2 as urllib
import json




# enter your credentials
access_token_key = "ENTER access_token_key HERE"
access_token_secret = "ENTER access_token_secret HERE"

consumer_key = "ENTER consumer_key HERE"
consumer_secret = "ENTER consumer_secret HERE"

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)



"""
Construct, sign, and open a twitter request
using the hard-coded credentials above.
"""
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response



  
"""
get the data from twitter api
"""
def fetchsamples():
    # api query, e.g. followers of januverma
    url = "https://api.twitter.com/1.1/followers/ids.json?screen_name=januverma"   
    parameters = []
    response = twitterreq(url, "GET", parameters)
    # response is a list of json objects, where each object contains the result of the query. 
    for line in response:
      # json decode the results, we get a python dictionary. 
      apple = json.loads(line)
      print apple["ids"]

     

if __name__ == '__main__':
  fetchsamples()


	

 

