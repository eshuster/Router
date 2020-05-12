import requests
import os

# class StravaOAuth:
#     def __init__(self, access_token=None, refresh_token=None):
#         self.access_token = access_token
#         self.client_secret = os.environ['STRAVA_CLIENT_SECRET']
#         self.client_id = os.environ['STRAVA_CLIENT_ID']
#         self.refresh_token = refresh_token
#
#     def refresh_token(self):
#         response = requests.get("https://www.strava.com/api/v3/oauth/token?client_id={}\
#                                        &client_secret={}&grant_type=refresh_token&refresh_token={}"
#                                 .format(self.client_id, self.client_secret, self.refresh_token))
#         self.access_token = response
#         self.refresh_token = response
#
#         return response
#
#     def authorize(self):
#         response = requests.get("https://www.strava.com/oauth/authorize?client_id={}&redirect_uri={}&\
#                                 response_type=code&approval_prompt=prompt&scope=activity:write,read"\
#                                 .format(self.client_id))
#         pass
#
#     def get_token(self):
#         response = requests.get("https://www.strava.com/api/v3/oauth/token?client_id={}\
#                                 &client_secret={}&grant_type=client_credentials"
#                                 .format(self.client_id, self.client_secret))
#         self.access_token = response
#         self.refresh_token = response
#
#         return response







