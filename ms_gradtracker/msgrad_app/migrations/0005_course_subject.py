# Generated by Django 4.1.4 on 2023-01-03 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msgrad_app', '0004_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='msgrad_app.subject'),
        ),
    ]
