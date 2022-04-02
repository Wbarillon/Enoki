from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone

from enoki_app.managers import (
    CustomUserManager
)


# Create your models here.

class CustomUser(PermissionsMixin, AbstractBaseUser):
    nickname = models.CharField(verbose_name = 'Pseudo', max_length = 50, unique = True)
    email = models.EmailField(unique = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(verbose_name = 'Date de création', default = timezone.now)

    USERNAME_FIELD = 'nickname'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Utilisateur (custom)'
        verbose_name_plural = 'Utilisateurs (custom)'

class Quiz(models.Model):

    id = models.AutoField(primary_key = True)
    subject = models.CharField(verbose_name = 'Sujet', max_length = 50, null = True, blank = True)
    version = models.PositiveSmallIntegerField(verbose_name = 'Version', null = True, blank = True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'

class Question(models.Model):

    id = models.AutoField(primary_key = True)
    id_quiz = models.ForeignKey('Quiz', on_delete = models.CASCADE, verbose_name = 'Questionnaire', null = False, blank = False)
    question = models.CharField(verbose_name = 'Question', max_length = 150, null = True, blank = True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class AnswerChoice(models.Model):

    id = models.AutoField(primary_key = True)
    id_quiz = models.ForeignKey('Quiz', on_delete = models.CASCADE, verbose_name = 'Questionnaire', null = False, blank = False)
    id_question = models.ForeignKey('Question', on_delete = models.CASCADE, verbose_name = 'Question', null = False, blank = False)
    answer_choice = models.CharField(verbose_name = 'Choix de réponses', max_length = 150, null = True, blank = True)
    correct_answer = models.BooleanField(verbose_name = 'Bonne réponse', null = True)

    def __str__(self):
        return self.answer_choice

    class Meta:
        verbose_name = 'Choix de réponse'
        verbose_name_plural = 'Choix de réponses'

class AnswerUser(models.Model):

    id = models.AutoField(primary_key = True)
    id_user = models.ForeignKey('CustomUser', on_delete = models.PROTECT, verbose_name = 'Utilisateur', null = False, blank = False)
    id_quiz = models.ForeignKey('Quiz', on_delete = models.CASCADE, verbose_name = 'Questionnaire', null = False, blank = False)
    id_question = models.ForeignKey('Question', on_delete = models.CASCADE, verbose_name = 'Question', null = False, blank = False)
    id_answer_choice = models.ForeignKey('AnswerChoice', on_delete = models.CASCADE, verbose_name = 'Choix de réponse', null = False, blank = False)

    def __str__(self):
        return self.id_user + - + self.id_answer_choice

    class Meta:
        verbose_name = 'Réponse des utilisateurs'
        verbose_name_plural = 'Réponses des utilisateurs'

class Score(models.Model):

    id = models.AutoField(primary_key = True)
    id_user = models.ForeignKey('CustomUser', on_delete = models.PROTECT, verbose_name = 'Utilisateur', null = False, blank = False)
    score = models.DecimalField(verbose_name = 'Score', max_digits = 3, decimal_places = 2, null = True, blank = True)

    def __str__(self):
        return self.id_user + - + score

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'