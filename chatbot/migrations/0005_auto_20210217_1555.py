# Generated by Django 3.1.1 on 2021-02-17 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_auto_20210217_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
    ]