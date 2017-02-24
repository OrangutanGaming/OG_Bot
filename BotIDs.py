clientID = ""
clientSecret = ""
username = ""
token = ""
permissionsURL = "" # https://finitereality.github.io/permissions/?v=0
OAuth2 = "https://discordapp.com/oauth2/authorize?permissions={}&scope=bot&client_id={}".format(permissionsURL, clientID)
URL = OAuth2

GitHubUser = ""
GitHubRepo = ""
GitHub = "https://github.com/{}/{}".format(GitHubUser, GitHubRepo)