# Generated by Django 4.0.3 on 2022-04-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enoki_app', '0004_answeruser_answer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeruser',
            name='answer_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de réponse'),
        ),
    ]