# Generated by Django 3.2.12 on 2022-02-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_alter_pricelookupevent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelookupevent',
            name='stock_name',
            field=models.CharField(default='aapl', max_length=20),
            preserve_default=False,
        ),
    ]
