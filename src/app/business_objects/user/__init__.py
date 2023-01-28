import uuid
from typing import Optional, List

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

    uid: str = Field(
        str(uuid.uuid4()),
        title="Unique identifier of the user"
    )

    phash: str = Field(
        None,
        title="Password hash"
    )

    salt: str = Field(
        None,
        title="Password salt"
    )

    name: str = Field(
        None,
        title="Name of the user"
    )

    last_name: str = Field(
        None,
        title="Last name of the user"
    )

    disabled: bool = Field(
        True,
        title="Weather the user is disabled or not. Disabled by default"
    )

    claims: Optional[List[str]] = Field(
        [
            'authenticate'
        ],
        title='User claims'
    )

    # -----------------------------------------------------
    # METHOD CAN
    # -----------------------------------------------------
    def can(self, claim: str) -> bool:
        """
        Validates if a particular claim is associated with
        given user
        :param claim: The claim to be verified
        :return: True is the user has the claim. False if the
        user does not have the claim
        """
        return claim in self.claims


# =========================================================
# CLASS ONLINE USER
# =========================================================
class UserSession(BaseModel):
    """
    Represents the session of an authenticated user
    """

    sub: str = Field(
        None,
        title=''
    )
    desc: str = Field(
        None,
        title=''
    )
    claims: List[str] = Field(
        None,
        title=''
    )
    exp: int = Field(
        None,
        title='Expiration of the session in Unix time'
    )

    # -----------------------------------------------------
    # METHOD CAN
    # -----------------------------------------------------
    def can(self, claim: str) -> bool:
        """
        Validates if a particular claim is associated with
        given user
        :param claim: The claim to be verified
        :return: True is the user has the claim. False if the
        user does not have the claim
        """
        return claim in self.claims




