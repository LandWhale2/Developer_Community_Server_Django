# Generated by Django 2.2.9 on 2020-01-07 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-timestamp',)},
        ),
    ]
