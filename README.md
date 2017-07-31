# Notify any Slack accoount by specified PTV disruption information 
Notify user of disruption information to their slack account

# How to use
```
  1. Download the project
  2. Change the certificate file to your own certificate information
  3. Change the Slack API token to your own account. Details about how to generate: https://api.slack.com/custom-integrations/legacy-tokens
  4. Run the main.py locally with the following command
        python main.py Userid Route Disruption_type
     - Userid: Could be a group or just a user For employer's information - add Barry, Harry, Wally, Freddy
     - Route: For employer's information - add Belgrave, Hurstbrdge, Werribee, or Frankston
     - Disruption_type: Can be either "planned" or "current"
```
# Output:
Your accont will receive a message including information as following:
```
If disruption:
  Disruption Information: .....
  Start time: ....
  End time: ....
```
```
If no disruption:
  "Good new! No disruption so far!!!!"
```
