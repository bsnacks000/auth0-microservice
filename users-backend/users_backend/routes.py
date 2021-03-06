from fastapi import APIRouter, Depends, Security
from .auth import Auth, Auth0User

router = APIRouter()

@router.get("/public")
async def get_public():
    return {"message": "Anonymous user"}

#route that only need client credentials
@router.get("/secure", dependencies=[Depends(Auth.implicit_scheme)])
async def get_secure(user: Auth0User = Security(Auth.get_user)):
    return {"message": f"{user}"}

#route with scopes
@router.get("/secure/users", dependencies=[Depends(Auth.implicit_scheme)])
async def get_secure_scoped(user: Auth0User = Security(Auth.get_user, scopes=["read:users"])):
    return {"message": f"{user}"}
