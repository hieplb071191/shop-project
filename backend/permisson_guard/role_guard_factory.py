from backend.permisson_guard.role_guard import RoleGuard

def RoleGuardWith(required_role: list[str]):
    class _RoleGuard(RoleGuard):
        def __init__(self):
            super().__init__(role_required=required_role)

    return _RoleGuard