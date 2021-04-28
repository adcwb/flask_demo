from application.utils import include

urlpatterns = [
    include("", "users.urls"),
]
