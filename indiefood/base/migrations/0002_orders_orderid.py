# Generated by Django 4.2.5 on 2023-10-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='orderId',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]