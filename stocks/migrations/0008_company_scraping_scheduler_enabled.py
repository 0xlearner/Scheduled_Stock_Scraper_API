# Generated by Django 3.2.12 on 2022-02-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_company_periodic_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='scraping_scheduler_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
