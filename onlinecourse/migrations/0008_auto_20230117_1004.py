# Generated by Django 3.1.3 on 2023-01-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0007_choice_choice_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(),
        ),
    ]