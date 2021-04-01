# Generated by Django 3.1.7 on 2021-04-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210330_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spot',
            name='y',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='spot',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
