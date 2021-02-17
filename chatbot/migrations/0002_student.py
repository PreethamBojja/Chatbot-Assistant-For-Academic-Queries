# Generated by Django 3.1.1 on 2021-02-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('roll_no', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('room_no', models.CharField(max_length=10)),
                ('hostel', models.CharField(max_length=12)),
            ],
        ),
    ]