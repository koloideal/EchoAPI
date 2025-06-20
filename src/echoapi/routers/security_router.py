from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm


security_router: APIRouter = APIRouter()

@security_router.post('/oauth2/token')
async def check_is_auth(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + 'case'}
