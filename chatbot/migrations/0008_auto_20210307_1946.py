# Generated by Django 3.1.1 on 2021-03-07 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_slot_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.slot'),
        ),
    ]