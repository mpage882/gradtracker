# Generated by Django 4.1.4 on 2023-01-09 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgrad_app', '0008_subject_total_credits_alter_subject_credit_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit_amount',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]