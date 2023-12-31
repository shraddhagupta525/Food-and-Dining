# Generated by Django 4.2.5 on 2023-10-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('items', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('noofperson', models.CharField(max_length=5)),
                ('tableType', models.CharField(max_length=20)),
                ('Time', models.DateTimeField(max_length=50)),
            ],
        ),
    ]
