# Generated by Django 2.1.5 on 2019-03-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=250)),
                ('subject_name', models.CharField(max_length=250)),
                ('course_number', models.CharField(max_length=30)),
                ('marks', models.IntegerField()),
                ('times', models.CharField(max_length=8)),
                ('total_questions', models.IntegerField(default=6)),
                ('to_be_answerd', models.IntegerField(default=4)),
            ],
        ),
    ]
