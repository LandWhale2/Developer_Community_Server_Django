# Generated by Django 2.2.9 on 2020-01-02 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191217_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.CharField(default=['qwe', 'qasd', 'asd'], max_length=255),
        ),
    ]