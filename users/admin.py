from django.contrib import admin
from .models import User,Student,Teacher
from django.contrib.auth.admin import UserAdmin
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []


class UserAdmin(admin.ModelAdmin):#UserAdmin):
    list_display_links = ('username',)
    list_display = ('username', 'is_staff', 'is_superuser',)
    fields = ('username','password','is_student','is_teacher')


class TeacherAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name',)
    fields = ('first_name', 'last_name', 'user')

class StudentAdmin(admin.ModelAdmin):
    # list_display_links = ('first_name', 'last_name')
    # list_display = ('first_name', 'last_name',)
    fields = ('user',)#('first_name', 'last_name', 'user')
    form = StudentForm

admin.site.register(User,UserAdmin)
admin.site.register(Student)#,StudentAdmin)
admin.site.register(Teacher)#,TeacherAdmin)
