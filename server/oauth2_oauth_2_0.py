# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from functools import wraps
from flask import g, request, jsonify

from jose import jwt

oauth2_server_pub_key = """"""

token_prefix = "Bearer "


def get_jwt_scopes(token, audience):
    return jwt.decode(token, oauth2_server_pub_key, audience=audience)["scope"]


class oauth2_oauth_2_0:
    def __init__(self, scopes=None, audience=None):
        self.allowed_scopes = scopes
        if audience is None:
            self.audience = ''
        else:
            self.audience = ",".join(audience)
        self.headers = ["Authorization", ]
        self.query_params = ["access_token", ]

    def __call__(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = self.get_token()

            if not token:
                return jsonify(), 401

            g.access_token = token

            if len(oauth2_server_pub_key) > 0:
                scopes = get_jwt_scopes(token, self.audience)
                if self.check_scopes(scopes) == False:
                    return jsonify(), 403
            return f(*args, **kwargs)
        return decorated_function

    def check_scopes(self, scopes):
        if self.allowed_scopes is None or len(self.allowed_scopes) == 0:
            return True

        for allowed in self.allowed_scopes:
            for s in scopes:
                if s == allowed:
                    return True

        return False

    def get_token(self):
        for header in self.headers:
            token = request.headers.get(header, "")
            if token.startswith(token_prefix):
                return token[len(token_prefix):]
        for param in self.query_params:
            token = request.args.get(param, "")
            if token:
                return token
