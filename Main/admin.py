from django.contrib import admin
from .models import form, zadachi, courses, Student
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Students'

# Define a new User admin


class UserAdmin(UserAdmin):
    inlines = (StudentInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(form)
admin.site.register(zadachi)
admin.site.register(courses)
