import certificate
import json, urllib, urllib2
import hmac, hashlib

#define a general function to integrate certificates
#define a optin for further development here
def call_ptv_api(api, option):
    args={}
    ptvbase = "http://timetableapi.ptv.vic.gov.au/v3/"
    version = "/v3/"
    args['devid'] = certificate.userid

    #for further development here, can have more requests
    if option == "routes":
        symbol = "?"
    elif option == "disruption":
        symbol = "&"

    call = version + api + symbol + urllib.urlencode(args)
    sig = hmac.new(certificate.apikey, call, hashlib.sha1).hexdigest().upper()
    url = ptvbase + call + "&signature=" + sig
    return json.load(urllib2.urlopen(url))

#get disruption information
def disruptions(route_id, option):
    disruptions = call_ptv_api("disruptions/route/"+ str(route_id) +"?disruption_status="+option ,"disruption")
    for disruption in disruptions["disruptions"].items():
        if len(disruption[1]) != 0:
            disruption_description = disruption[1][0]["description"]
            disruption_from_date = disruption[1][0]["from_date"]
            disruption_to_date = disruption[1][0]["to_date"]
            return disruption_description, disruption_from_date,disruption_to_date

#get route id based on the route name
def get_routes(input_route_name):
    routes = call_ptv_api("routes","routes")
    for route in routes["routes"]:
        if route["route_name"] == input_route_name:
            return route["route_id"]
