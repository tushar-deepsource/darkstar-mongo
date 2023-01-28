from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status

from app.business_objects.user import Users
from app.security import IdentityCredential
from app.security.cryptography import Password
from app.context import get_context
from app.business_objects.user import inject_users

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"/api/{get_context().api_version}/auth/token"
)


# ---------------------------------------------------------
# CLASS USER AUTHENTICATION
# ---------------------------------------------------------
class UserAuthentication:
    """
    A user authentication is the process of determining if a
    given set of credentials are valid for a particular user.
    This class can be extended to support other authentication
    schemas.
    """

    # -----------------------------------------------------
    # CONSTRUCTOR METHOD
    # -----------------------------------------------------
    def __init__(
            self,
            username: str,
            password: str,
            users: Users = inject_users()
    ):
        self.username: str = username
        self.password: str = password
        self.users: Users = users
        self.user_data: dict or None = self.__user_data

    # -----------------------------------------------------
    # DESTRUCTOR METHOD
    # -----------------------------------------------------
    def __del__(self):
        """
        Cleans values in memory before releasing memory
        back to the operating system.
        :return: None
        """
        self.password = 0000000000000000000000000000000000
        self.username = 0000000000000000000000000000000000
        self.user_data = 000000000000000000000000000000000

    # -----------------------------------------------------
    # METHOD RETRIEVE USER DATA
    # -----------------------------------------------------
    @property
    def __user_data(self) -> dict:
        """
        Retrieves the user data from the database using the
        users' repository.
        :return: Dict
        """
        return self.users.get_by_username(
            self.username
        )

    # -----------------------------------------------------
    # VERIFY PASSWORD
    # -----------------------------------------------------
    @staticmethod
    def __verify_password(
            password: str,
            password_hash: str,
            salt: str
    ) -> bool:
        """
        Verifies if a given password is valid
        :param password: The password to be verified
        :param password_hash: The hash of the password stored
        in the internal user database
        :param salt: salt to link password to this specific
        context and prevent rainbow table attacks
        :return: True if password is valid / False if password
        is not valid
        """
        credential: IdentityCredential = Password(
            plain_text_password=password,
            salt=salt
        )
        return credential.verify(
            stored_hash=password_hash
        )

    # -----------------------------------------------------
    # PROPERTY IS VALID
    # -----------------------------------------------------
    @property
    def is_valid(self) -> bool:
        return False
