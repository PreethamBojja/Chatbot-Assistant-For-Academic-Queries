# Generated by Django 3.1.1 on 2021-03-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0016_registeredcourses_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcourses',
            name='attendance',
            field=models.IntegerField(),
        ),
    ]