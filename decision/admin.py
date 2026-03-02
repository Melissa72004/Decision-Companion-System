from django.contrib import admin
from .models import Decision, Criteria, Option, Score

admin.site.register(Decision)
admin.site.register(Criteria)
admin.site.register(Option)
admin.site.register(Score)