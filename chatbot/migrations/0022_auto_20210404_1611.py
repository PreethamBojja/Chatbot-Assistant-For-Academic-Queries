# Generated by Django 3.1.1 on 2021-04-04 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0021_auto_20210404_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationdetails',
            options={'verbose_name_plural': 'Registration Details'},
        ),
        migrations.RemoveField(
            model_name='registrationdetails',
            name='branch',
        ),
        migrations.AddField(
            model_name='registrationdetails',
            name='dept',
            field=models.ForeignKey(default='MNC', on_delete=django.db.models.deletion.CASCADE, to='chatbot.department'),
        ),
    ]