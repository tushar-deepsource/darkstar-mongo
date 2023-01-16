from typing import List
from app.cdb.repository import HeimdallEntityRepository


# =========================================================
# CLASS BENCHMARKS
# =========================================================
class SecurityCenterRepositories(HeimdallEntityRepository):

    # -----------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------
    def __init__(self):
        super().__init__(
            collection_name='sc_repositories'
        )

    # -----------------------------------------------------
    # GET INDEX FIELDS
    # -----------------------------------------------------
    def get_index_fields(self) -> List[str]:
        return [
            'repository_id'
        ]


# =========================================================
# FUNCTION INJECT SECURITY CENTER REPOSITORIES
# =========================================================
def inject_security_center_repositories() -> SecurityCenterRepositories:
    return SecurityCenterRepositories()
