# Generated by Django 4.1.4 on 2023-01-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgrad_app', '0003_rename_subjects_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('credit_amount', models.IntegerField()),
            ],
        ),
    ]
