import requests
##change this token 
tok = 'EAAZAUYSkc89EBABZAJahTV6FlseUClYrzLQIcjepeBZA5hxy0B8wrLZBDRaZBTQ14COZCr05yPCO0Wu6TAzG8OMO1d7x6MBUsg7zz2L2kZBQUqu1N9Mh7ZA1Fl2zLOUD96D7Y9yKh6pZAJrLbqZBRxMNVuDv4rr8AHzvP7JebETsx3ixCBwEq5JFfsBY0HTJGja38ZD'
##change this group id
groupid = '325608301293894'
##change this field 
fields = 'member_count'
req = groupid + '?fields=' + fields

posts = requests.get('https://graph.facebook.com/v3.0/' + req , {'access_token' : tok})
poo = posts.json()
##print(poo['posts'])
print(posts.text)
##go to terminal and run the python application 
##and there we got the facebook api information thanks for watching!