from rest_framework.permissions import IsAuthenticated

class AuthGuard(IsAuthenticated):
    def __init__(self):
        super().__init__()
        self.message = "Bạn cần đăng nhập để truy cập API này."
        print(self)

    def __str__(self):
        return f"AuthGuard(message='{self.message}')"

    def __repr__(self):
        return self.__str__()