import requests
##change this token 
tok = ''
##change this group id
groupid = ''
##change this field 
fields = ''
req = groupid + '?fields=' + fields

posts = requests.get('https://graph.facebook.com/v3.0/' + req , {'access_token' : tok})
poo = posts.json()
##print(poo['posts'])
print(posts.text)
##go to terminal and run the python application using the command "python facebookinfo.py"