from django.contrib import admin
from .models import *

# to add question and answer all in one screen we use Inlinemodel
# so when I make question I can build answer straight away
# TabularInline allows us to build up different tables together to build data consecutively
class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer',
        'is_correct'
    ]

# Now we have to take AnswerInlineModel table and tell django to stitch this table with Question table together
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'points',
        'difficulty',
    ]
    list_display = [
        'title',
        'updated_at',
    ]
    # this puts the answer underneath it- doing that when i add question it will associate it to those answers that i enter
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question'
    ]