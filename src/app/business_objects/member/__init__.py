from app.business_objects.member.repository import Members


# =========================================================
# FUNCTION INJECT USERS
# =========================================================
def inject_members() -> Members:
    return Members()
