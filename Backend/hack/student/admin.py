from django.contrib import admin
from .models import notes, profile, Question, Answer, JoinUs

# Register your models here.

admin.site.register(notes)
admin.site.register(profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(JoinUs)