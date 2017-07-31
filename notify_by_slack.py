import urllib, urllib2

#notify user by slack api Tester
#generate your own api token for later use
def call_slack_api(user, message):
    slack_base = "https://slack.com/api/"
    api_token = "chat.postMessage?token=xoxp-219773863122-220665630998-220670148582-d9471c6d4f68cdfd0cb6a68ccd32275d"
    args = {"channel":"@"+user, "text":message}
    url = slack_base + api_token + "&" + urllib.urlencode(args)
    urllib2.urlopen(url)


