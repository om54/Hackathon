# Generated by Django 4.0.2 on 2022-03-22 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='desc',
            new_name='message',
        ),
    ]
