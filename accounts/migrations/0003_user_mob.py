# Generated by Django 3.1.5 on 2021-03-14 17:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mob',
            field=models.TextField(default=datetime.datetime(2021, 3, 14, 17, 6, 49, 665196, tzinfo=utc), max_length=30, unique=True),
            preserve_default=False,
        ),
    ]