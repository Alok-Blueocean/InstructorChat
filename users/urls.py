from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,StudentViewSet,TeacherViewSet,StudentCreateView

router = DefaultRouter()

router.register(r'students',StudentViewSet)
router.register(r'teachers',TeacherViewSet)
router.register(r'',UserViewSet)

urlpatterns = [

path(r'',include(router.urls)),
path(r'register',StudentCreateView.as_view(),name = 'register')
]