# Generated by Django 3.1.3 on 2023-01-17 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_choice_submission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
    ]