from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from bson import ObjectId
from db import users
from auth_utils import verify_token

bearer = HTTPBearer(auto_error=False)

async def require_auth(creds=Depends(bearer)):
    if not creds:
        raise HTTPException(status_code=401)
    try:
        payload = verify_token(creds.credentials)
    except:
        raise HTTPException(status_code=401)

    user = await users.find_one({"_id": ObjectId(payload["sub"])}, {"passwordHash": 0})
    if not user:
        raise HTTPException(status_code=401)

    user["id"] = str(user["_id"])
    return user

def require_admin(user=Depends(require_auth)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403)
    return user
