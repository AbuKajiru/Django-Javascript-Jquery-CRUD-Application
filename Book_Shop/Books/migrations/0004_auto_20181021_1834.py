# Generated by Django 2.1.2 on 2018-10-21 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_auto_20181021_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybooks',
            name='Description',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='mybooks',
            name='Date_Added',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 21, 18, 34, 47, 572308)),
        ),
    ]