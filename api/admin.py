from django.contrib import admin
from .models import Question,Answer,AnswerRequest,AnswerResponse

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerRequest)
admin.site.register(AnswerResponse)
