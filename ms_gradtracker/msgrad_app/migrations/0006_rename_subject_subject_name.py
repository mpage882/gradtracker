# Generated by Django 4.1.4 on 2023-01-03 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgrad_app', '0005_course_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='name',
        ),
    ]
