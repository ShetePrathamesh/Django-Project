# Generated by Django 3.2.9 on 2021-12-15 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_auto_20211215_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='Id',
        ),
    ]
