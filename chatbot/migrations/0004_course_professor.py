# Generated by Django 3.1.1 on 2021-03-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_registrationdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('prof_name', models.TextField(primary_key=True, serialize=False)),
                ('room_no', models.CharField(max_length=7)),
                ('research_area', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.department')),
            ],
            options={
                'verbose_name_plural': 'Professor',
            },
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_name', models.CharField(max_length=30)),
                ('course_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('slot', models.CharField(max_length=2)),
                ('course_venue', models.CharField(max_length=8)),
                ('course_content', models.URLField()),
                ('attendance', models.IntegerField()),
                ('grading_schema', models.CharField(max_length=300)),
                ('course_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.professor')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
    ]