import twitter, datetime, urllib2 #Importing Twitter library

currentSession = open("/Users/student/Library/Application Support/Google/Chrome/Default/Current Session") #open chrome browsing history

lastSession = currentSession.read() #Reads the info from last session

user = 173585457 #My Twitter account ID

file = open("API-key.txt") #Opens access token files

cred = file.readline().strip().split(",") #Reads the credentials 

startIndex = lastSession.rfind("http")
endIndex = lastSession.find(chr(0), startIndex) #Stars and ends index's of previous session

url = lastSession[startIndex:endIndex] #Preparing last session address
print(url)

urlreceived = urllib2.urlopen(url) 
html = urlreceived.read()

beginTitle = html.find("<title>") + len("<title>") 
finishTitle = html.find("</title>", beginTitle)
theTitle = html[beginTitle:finishTitle] #Loads title of page


api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
		  access_token_key=cred[2],access_token_secret=cred[3]) #Confirming api information

timestamp = datetime.datetime.utcnow() 

response = api.PostUpdate("Today I have been to " + url + " in " + str(timestamp) + " Title is: " + str(theTitle)) #posts web pege url, time and date and page title

print("Status updated to: " + response.text) 

statuses = api.GetUserTimeline(user) #Posts previous Twitter status into terminal
print (statuses[0].text)