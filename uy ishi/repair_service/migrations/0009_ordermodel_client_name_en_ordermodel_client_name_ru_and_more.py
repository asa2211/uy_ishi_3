# Generated by Django 4.2.4 on 2023-08-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_service', '0008_ustamodel_mutaxasislig_en_ustamodel_mutaxasislig_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='client_name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='client_name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='client_name_uz',
            field=models.CharField(max_length=50, null=True),
        ),
    ]