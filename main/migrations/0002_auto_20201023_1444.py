# Generated by Django 2.2 on 2020-10-23 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='email_address',
            field=models.CharField(default='no email', max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='phone_number',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
