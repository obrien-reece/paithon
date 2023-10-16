from django.contrib import admin
from .models import Question, Choice

# This particular change above makes the
# “Publication date” come before the “Question” field:


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


admin.site.register(Question)
admin.site.register(Choice)
