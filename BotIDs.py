clientID = ""
clientSecret = ""
username = ""
token = ""
permissionsURL = ""
OAuth2 = "https://discordapp.com/oauth2/authorize?permissions={}&scope=bot&client_id={}".format(permissionsURL, clientID)
URL = OAuth2
print(URL)
