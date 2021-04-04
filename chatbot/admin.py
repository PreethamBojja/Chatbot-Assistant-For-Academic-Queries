from django.contrib import admin
from .models import department,course,RegistrationDetails,Professor,student,Slot,TimeTable,RegisteredCourses
# Register your models here.


admin.site.register(RegistrationDetails)
admin.site.register(student)
admin.site.register(Professor)
admin.site.register(department)
admin.site.register(course)
admin.site.register(Slot)
admin.site.register(TimeTable)
admin.site.register(RegisteredCourses)
