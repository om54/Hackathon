# Generated by Django 4.0.2 on 2022-03-25 13:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
