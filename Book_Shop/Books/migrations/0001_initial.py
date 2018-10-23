# Generated by Django 2.1.2 on 2018-10-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Author', models.CharField(max_length=250)),
                ('Publisher', models.CharField(max_length=250)),
                ('Year_Of_Publication', models.IntegerField(default=2018)),
                ('No_Of_Copies', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='myDeletedBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Author', models.CharField(max_length=250)),
                ('Publisher', models.CharField(max_length=250)),
                ('Year_Of_Publication', models.IntegerField(default=2018)),
            ],
        ),
    ]