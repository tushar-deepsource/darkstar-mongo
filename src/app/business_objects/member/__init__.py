from app.business_objects.member.repository import Members


# =========================================================
# FUNCTION INJECT MEMBERS
# =========================================================
def inject_members() -> Members:
    return Members()
