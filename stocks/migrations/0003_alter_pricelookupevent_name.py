# Generated by Django 3.2.12 on 2022-02-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_alter_company_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelookupevent',
            name='name',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
