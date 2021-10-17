from fastapi_auth0 import Auth0, Auth0User
from .config import AUTH0_DOMAIN, AUTH0_API_AUDIENCE

#fastapi_auth0 libary dependecies; the library will internally read AUTH0_RULE_NAMESPACE from .env
Auth = Auth0(domain=AUTH0_DOMAIN, api_audience=AUTH0_API_AUDIENCE, scopes={
    'read:users': 'Read BlaBla resource'
})