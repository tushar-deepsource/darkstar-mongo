from typing import Optional

from app.business_objects.user.repository import Users
from pydantic import BaseModel, Field


# =========================================================
# FUNCTION INJECT USERS
# =========================================================
def inject_users() -> Users:
    return Users()


# =========================================================
# CLASS USER
# =========================================================
class User(BaseModel):

    _id: Optional[str] = Field(
        None,
        title='Internal Identifier'
    )


