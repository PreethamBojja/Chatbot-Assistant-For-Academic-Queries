# Generated by Django 3.1.1 on 2021-03-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_course_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.CharField(default='MA 252/MA 512', max_length=10),
        ),
    ]