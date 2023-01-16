from typing import List

from app.cdb.repository import HeimdallEntityRepository


# =========================================================
# CLASS BENCHMARKS
# =========================================================
class Benchmarks(HeimdallEntityRepository):

    # -----------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------
    def __init__(self):
        super().__init__(
            collection_name='benchmarks'
        )

    # -----------------------------------------------------
    # GET INDEX FIELDS
    # -----------------------------------------------------
    def get_index_fields(self) -> List[str]:
        return [
            'id'
        ]


# =========================================================
# FUNCTION INJECT BENCHMARKS
# =========================================================
def inject_benchmarks() -> Benchmarks:
    return Benchmarks()
