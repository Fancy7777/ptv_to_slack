import ptv
import datetime
import sys
import notify_by_slack

#pass the arguments by command line so far
if __name__ == "__main__":
    sending_user = sys.argv[1]
    route = sys.argv[2]
    option = sys.argv[3]
    try:
        description, start_time, end_time = ptv.disruptions(ptv.get_routes(route), option)
        disruption_start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
        disruption_end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")
        message = "Disruption Information: " + description.encode('utf-8') + '\n' + "Start time: " + str(

        disruption_start_time) + '\n' + "End time: " + str(disruption_end_time)
        notify_by_slack.call_slack_api(sending_user, message)
    except TypeError:
        message = "Good new! No disruption so far!!!!"
        notify_by_slack.call_slack_api(sending_user, message)
