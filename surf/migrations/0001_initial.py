# Generated by Django 3.1.7 on 2021-03-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot', models.CharField(max_length=100)),
                ('planned', models.IntegerField(default=0)),
            ],
        ),
    ]
