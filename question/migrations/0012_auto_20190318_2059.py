# Generated by Django 2.1.5 on 2019-03-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0011_auto_20190318_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='marks',
            field=models.IntegerField(default=(1, 2, 3, 4, 5, 6, 7, 8, 9)),
        ),
    ]
