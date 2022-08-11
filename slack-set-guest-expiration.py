import os
import logging
import logging.handlers
import slack_sdk
import csv
from csv import DictReader
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#Logs script output for review
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "slack-expiration.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
root.addHandler(handler)

#Prompt for location of CSV file with userids
get_guest_users_list_location = input("Where is your Guest User CSV file located?: ")
guest_users = get_guest_users_list_location

#Prompt for the desired expiration date
print("When would you like the account to expire?")
expiration_date = input("Date should be entered in Epoch Time. An Epoch Time converter can be found at https://www.epochconverter.com/: ")
expiration_time = expiration_date

#Update this value with your slack token 
client = WebClient(token='')

#Function that sets the expiration date. Update the team_id value with your team id (optional, per slack documentation)
def set_expiration():
    with open(f'{guest_users}') as user_list:
        users = DictReader(user_list)
        for user in users:
            guest_user = (user['userid'])
            response = client.admin_users_setExpiration(user_id=f"{guest_user}", expiration_ts=f"{expiration_time}", team_id="")
set_expiration()