from typing import Any, Optional
from fastapi import APIRouter
import json
import os
import boto3

router = APIRouter()

@router.post("/")
def set_credentials(access_key: str, secret_key: str, session_token: str = None, session_timeout: str = None) -> Any:
    os.environ["AWS_ACCESS_KEY_ID"] = access_key
    os.environ["AWS_SECRET_ACCESS_KEY"] = secret_key
    if session_token:
        os.environ["AWS_SESSION_TOKEN"] = session_token
        if session_timeout:
            os.environ["AWS_TOKEN_EXPIRATION"] = session_timeout
    client = boto3.client('sts')
    return client.get_caller_identity()