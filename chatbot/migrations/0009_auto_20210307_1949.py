# Generated by Django 3.1.1 on 2021-03-07 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_auto_20210307_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dept_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.department'),
        ),
    ]