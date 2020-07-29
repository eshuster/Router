from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.django_client import OAuth
oauth = OAuth()

class OAuthMixin:
    def authorize(self, client, client_secret, auth_url, access_token_url, redirect_url, client_id):
        uri, state = client.create_authorization_url(url=auth_url, scope="read", response_type="code", redirect_uri=redirect_url, approval_prompt="force")

        return uri

    def get_token(self, client, access_token_url, authorization_response, code, client_id, client_secret):
        access_token_url = access_token_url + "?&client_id=" + str(client_id) + "&client_secret=" + client_secret + "&grant_type=authorization_code&code=" + code
        token = client.fetch_token(access_token_url, authorization_response=authorization_response)

        return token