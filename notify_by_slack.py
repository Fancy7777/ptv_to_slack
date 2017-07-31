import urllib, urllib2

#notify user by slack api Tester
#generate your own api token for later use
def call_slack_api(user, message):
    slack_base = "https://slack.com/api/"

    #add your own api-token here
    api_token = "example"
    args = {"channel":"@"+user, "text":message}
    url = slack_base + api_token + "&" + urllib.urlencode(args)
    urllib2.urlopen(url)


