from typing import List

from authlib.integrations.starlette_client import OAuth
from authlib.oidc.core import UserInfo
from app.context import get_context
import uuid


# --------------------------------------------------------
# GET OR DEFAULT
# --------------------------------------------------------
class Identity:
    def __init__(self, user_info: UserInfo):
        self.name: str = self.__get_or_default(user_info.get("name"))
        self.uid: str = self.__get_or_default(user_info.get("uid"))
        self.email: str = self.__get_or_default(user_info.get("email")).lower()
        self.s_hash: str = self.__get_or_default(user_info.get("s_hash")).lower()
        self.challenge: str = self.__gen_challenge()

    @staticmethod
    def __gen_challenge() -> str:
        return str(uuid.uuid4()).replace("-", "#").upper()

    def dict(self) -> dict:
        return {
            "name": self.name,
            "uid": self.uid,
            "email": self.email,
            "s_hash": self.s_hash,
            "challenge": self.challenge,
        }

    @staticmethod
    def __get_or_default(value: str) -> str:
        if value is None or value == "":
            return "n/a"
        return value


# --------------------------------------------------------
# REGISTER AND GET OAUTH PROVIDER
# --------------------------------------------------------
def get_oauth() -> OAuth:
    provider = OAuth()
    config = get_context()
    provider.register(
        name="authentik",
        server_metadata_url=get_context().oidc_discovery_endpoint,
        client_id=get_context().oidc_client_id,
        client_secret=get_context().oidc_client_secret,
        client_kwargs={"scope": "openid email profile"},
    )
    return provider
