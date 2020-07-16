from rest_framework.routers import DefaultRouter
from REST.views import UserViewSet, GroupViewSet, BookViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'groups',GroupViewSet)
router.register(r'book',BookViewSet)