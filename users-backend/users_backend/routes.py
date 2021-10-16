from fastapi import APIRouter, Depends, Security
from .auth import Auth, Auth0User

router = APIRouter()

@router.get("/public")
async def get_public():
    return {"message": "Anonymous user"}

@router.get("/secure", dependencies=[Depends(Auth.implicit_scheme)])
async def get_secure(user: Auth0User = Security(Auth.get_user)):
    return {"message": f"{user}"}

@router.get("/secure/users", dependencies=[Depends(Auth.implicit_scheme)])
async def get_secure_scoped(user: Auth0User = Security(Auth.get_user, scopes=["read:users"])):
    return {"message": f"{user}"}


@router.get("/secure/users2")
async def get_secure_scoped2(user: Auth0User = Security(Auth.get_user, scopes=["read:users"])):
    return {"message": f"{user}"}