# Generated by Django 2.1.1 on 2018-10-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_url', models.CharField(max_length=200)),
            ],
        ),
    ]
