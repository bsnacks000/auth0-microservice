### Micorservices with Auth0

#### Users API
* FastAPI backend for users resources 

#### Users Frontend
* React frontend 

### Auth0 Configuration
#### Users API
* Create an API in Auth0's `Applications.APIs`; Set `Identifier`found in `Applications.APIs.<API_NAME>.Settings` as `AUTH0_API_AUDIENCE` in .env, and `Domain` found in `Applications.Application.<API_NAME>.Settings` as `AUTH0_DOMAIN`.
* Add permission scope `read:users` in `Applications.APIs.<API_NAME>.Permissions`. Add another permission scope
`openid profile email` to get access to user's email and profile.
* To include permissions in access token, enable `Add Permissions in the Access Token` via `Applications.Applications.APIs.<API_NAME>.Settings.RBAC Settings`.
* Enable auth rule `Add email to access token` in `Auth Pipeline.Rules`; if not found, the rule can be created via
rule template in create rule menu; it is under `Access Control` section.
* To add email to access token, a nampespace must be defined. Click on `Add email to access token` rule to edit the script
and give a value to namespace. Make sure that the namespace string ends with `/`; for example, `var namespace = http://namespace.blah.com/`. The slash at the end is needed since model field defined in `fastapi_auth0` is `f{namesampce}/email`.
Now set `namespace` without the ending slash  as `AUTH0_RULE_NAMESPACE` in .env; for example, `AUTH0_RULE_NAMESPACE=http://namespace.blah.com`. `fastapi_auth0 will` read in `AUTH0_RULE_NAMESPACE` value from enviroment. See [here](https://community.auth0.com/t/include-email-in-jwt/39778) 

#### REACT APP (SPA)
* Create an SPA application in Auth0's `Applications.Applications`; set `Domain` found in `Applications.Application.<API_NAME>.Settings` as `REACT_APP_AUTH0_DOMAIN` and `Client ID` as `REACT_APP_AUTH0_CLIENT_ID`; and `AUTH0_API_AUDIENCE` from API's .env as `REACT_APP_AUTH0_AUDIENCE`.
* Make sure that scopes/permissions declared in APIs are also provided in `Auth0Provider`. See `users-frontend/src/auth/Auth0ProviderWithHistory` and [here](https://auth0.com/blog/complete-guide-to-react-user-authentication/#Calling-an-API)(scopes are talked about near the end of 'Calling an API' section). Multiple scopes can be provided by separating with a space.
* Set API url as `REACT_APP_SERVER_URL` in .env

**Note** Permissions are configured differently for Machine to Machine Application. Permissions can be added via `Applications.Applications.<Machine to Machine App name>.APIs`. Requesting for access token for machine to machine application can be tested via  `Applications.APIs.<API_NAME>.Test`.

#### Users
* Users can be created and assigned permissions via Auth0's `User Manangement.Users`.
* After a user is created, desired permission must be added manually for that user for relevant API. And a new token must be
requested again for the changes to take place.