from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status

from app.business_objects.user import Users, UserSession
from app.security import IdentityCredential
from app.security.cryptography import Password
from app.context import get_context, ServerContext
from app.business_objects.user import inject_users

from jose import jwt, JWTError

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


# ---------------------------------------------------------
# FUNCTION GET CREDENTIALS EXCEPTION
# ---------------------------------------------------------
def get_credentials_exception() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unable to validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )


# ---------------------------------------------------------
# FUNCTION GETY CURRENT USER
# ---------------------------------------------------------
async def get_user_session(
        token: str = Depends(oauth2_schema),
        context: ServerContext = Depends(get_context)
) -> UserSession:
    """
    Given a valid JWT access token, this functions decodes
    the token and validates its digital signature
    :param token: The encoded JWT access token fetched from
    the Authorization header in the HTTP Request
    :param context: Server context to securely access
    the signing keys
    :return:
    """
    try:
        payload = jwt.decode(
            token=token,
            key=context.jwt_key,
            algorithms=[context.jwt_signing_algorithm]
        )
        key_id: str = payload.get('sub')
        if key_id is None:
            raise get_credentials_exception()
    except JWTError:
        raise get_credentials_exception()

    session: UserSession = UserSession(**payload)
    if session is None:
        raise get_credentials_exception()
    context.logging.debug(f'User: {session.dict()} successfully authenticated')
    return session
