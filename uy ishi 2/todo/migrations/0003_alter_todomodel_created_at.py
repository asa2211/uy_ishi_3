# Generated by Django 4.2.3 on 2023-08-23 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todomodel_task_name_en_todomodel_task_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]