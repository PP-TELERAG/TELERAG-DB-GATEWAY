import hmac

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.settings.config import settings


security = HTTPBasic()


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):

    if hmac.compare_digest(
        credentials.username, settings.ACCESS_USERNAME
    ) and \
            hmac.compare_digest(
                credentials.password, settings.ACCESS_PASSWORD
    ):
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
