from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet,AnswerViewSet,AnswerRequestViewSet,AnswerResponseViewSet


router = DefaultRouter()
router.register('questions',QuestionViewSet)
router.register('answers',AnswerViewSet)
router.register('answer_requests',AnswerRequestViewSet)
router.register('answer_responses',AnswerResponseViewSet)

urlpatterns = router.urls