# Generated by Django 3.1.1 on 2021-04-04 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0020_course_dept_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dept_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.department'),
        ),
    ]