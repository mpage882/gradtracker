# Generated by Django 4.1.4 on 2023-01-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgrad_app', '0006_rename_subject_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='gpa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
