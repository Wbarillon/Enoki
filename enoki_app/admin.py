from django.contrib import admin

from enoki_app.models import (
    AnswerChoice,
    AnswerUser,
    CustomUser,
    Question,
    Quiz,
    Score
)

# Register your models here.

from django.contrib import admin

@admin.register(AnswerChoice)
class AnswerChoiceAdmin(admin.ModelAdmin):
    list_display = [element.name for element in AnswerChoice._meta.fields]

@admin.register(AnswerUser)
class AnswerUserAdmin(admin.ModelAdmin):
    list_display = [element.name for element in AnswerUser._meta.fields]

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Fields are sliced in order to not display password field.
    list_display = [element.name for element in CustomUser._meta.fields[:1] + CustomUser._meta.fields[2:]]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [element.name for element in Question._meta.fields]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [element.name for element in Quiz._meta.fields]

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = [element.name for element in Score._meta.fields]