from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,StudentViewSet,TeacherViewSet

router = DefaultRouter()

router.register(r'students',StudentViewSet)
router.register(r'teachers',TeacherViewSet)
router.register(r'',UserViewSet)

urlpatterns = router.urls
