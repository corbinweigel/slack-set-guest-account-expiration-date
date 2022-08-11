# Slack - Bulk Set Guest Account Expiration Date
A Python script to bulk update the expiration date of guest users via the CSV file exported from the Slack Admin Console

## What does this script do? 
This script reads a CSV file with Slack User IDs and updates the selected IDs with a specified expiration date. 

## How do I use this script? 
First, you'll need to fullfil the requirements... 

### Requirements: 
- Python 3.9.1 (Older versions may work, but this is the version I wrote it in)
- Slack SDK for Python [(Python Slack SDK)](https://slack.dev/python-slack-sdk/)
- A Slack API Token [(Create A Token)](https://github.com/slackapi/python-slack-sdk/blob/main/tutorial/01-creating-the-slack-app.md)
    - Required Scopes: 
        - admin.users:write
        - admin.users:read
- A CSV file with your User IDs in it, with "userid" as the column header

 ### Requirements set! Now what? 
 Great! Now you will want to... 
 - Set ```client = WebClient(token='')``` equal to the Slack Token you generated earlier, or pull it in from your OS Environment, if you decided to go that route
 - Prep your CSV file 
     - If you don't already have it handy, a CSV file with all users can esaily be exported from the [Slack Admin Console](https://slack.com/admin)
     - Make sure to filter for Guests and Multi-Channel Guest accounts and paste them into a new spreadsheet before running the script!
 - Determine the expiration date, in [Epoch Time](https://www.epochconverter.com/)
 
 ### Running the script
 With all your requirements and prep in place, you'll now want to run the script! You can do that by...
 - Executing the following command from your terminal: ```python slack-set-guest-expiration.py```
     - Pasting in the location of your CSV file when prompted, e.g.: ```/Users/corbin/Downloads/slack-guest-users.csv```
     - Pasting in the time the accounts should expire, in Epoch format, e.g.: ```1660067652```    
     
 The script should now run and iterate through your list, setting the expiration date for the userid of the Guest Accounts listed in your spreadsheet    
 
 ## Notes:
 - Nothing is output to the console, but everything is logged to ```slack-expiration.log```, which will be created in the directory the script is run from
 - I have not built in any error handling to look for exceptions, so if something other than a CSV file is passed into the script, or the wrong time format is used, the script will blow up. Fortunately, this script can't really cause too much damage with the API call being made
 - More information on this particular Slack API call can be found [here](https://api.slack.com/methods/admin.users.setExpiration)
     - Please note that once an expiration date is set, the only way to unset it, is manually. I played around with different values for the ```expiration_ts``` value, and none would clear out the expiration date. Although you can set it 200+ years in the future with ```9999999999```...
 - There's plenty of room for improvement on this script, so feel free to fork it or make suggestions! I just needed something quick and dirty that would save me from a few hours of manual clicky clicky in the Slack Admin Console
 - **This script requires Enterprise Grid or equivalent to function correctly**
 - I take no responsibility for breaking your Slack instance if you use this script. Like all random scripts found on the internet, they should be read through before randomly running them against your Production Environment ;)
