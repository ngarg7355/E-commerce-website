# Generated by Django 3.0.5 on 2020-05-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0003_auto_20200523_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
