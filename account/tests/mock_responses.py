def strava_authorization_url():
    return "https://www.strava.com/oauth/authorize?response_type=code&" \
           "client_id=41327&redirect_uri=http%3A%2F%2F"

def get_strava_oauth_token():
    return {
        'token_type': 'Bearer',
        'expires_at': 1596284800,
        'expires_in': 21571,
        'refresh_token': '055c9385632cb31d9913af3ce9c60d4d86ad6fd1',
        'access_token': 'e8adce95e7f1a18a9e3cf6e85b035a4eb4f7d4bb',
        'athlete': {
            'id': 33543585,
            'username': 'yevgeniy_shuster',
            'resource_state': 2,
            'firstname': 'Yevgeniy',
            'lastname': 'Shuster',
            'city': 'San Francisco',
            'state': 'California',
            'country': 'United States',
            'sex': 'M',
            'premium': True,
            'summit': True,
            'created_at': '2018-08-07T19:20:15Z',
            'updated_at': '2020-07-23T18:02:30Z',
            'badge_type_id': 1,
            'profile_medium': 'https://graph.facebook.com/10156559907786764/picture?height=256&width=256',
            'profile': 'https://graph.facebook.com/10156559907786764/picture?height=256&width=256',
            'friend': None,
            'follower': None
        }
    }