from typing import Any, Optional
from fastapi import APIRouter
from pydantic import BaseModel
import json
import os
import boto3

class CredentialBody(BaseModel):
    access_key: str
    secret_key: str
    session_token: str = None
    session_timeout: str = None
    region: str = 'us-east-1'


router = APIRouter()

@router.post("/")
def set_credentials(credential_body: CredentialBody) -> Any:
    os.unsetenv("AWS_DEFAULT_REGION")
    os.unsetenv("AWS_ACCESS_KEY_ID")
    os.unsetenv("AWS_SECRET_ACCESS_KEY")
    os.unsetenv("AWS_SESSION_TOKEN")
    os.unsetenv("AWS_TOKEN_EXPIRATION")

    os.environ["AWS_DEFAULT_REGION"] = credential_body.region
    os.environ["AWS_ACCESS_KEY_ID"] = credential_body.access_key
    os.environ["AWS_SECRET_ACCESS_KEY"] = credential_body.secret_key
    if credential_body.session_token:
        os.environ["AWS_SESSION_TOKEN"] = credential_body.session_token
        if session_timeout:
            os.environ["AWS_TOKEN_EXPIRATION"] = credential_body.session_timeout
    client = boto3.client('sts')
    return client.get_caller_identity()

@router.get("/")
def get_credentials():
    client = boto3.client('sts')
    return client.get_caller_identity()