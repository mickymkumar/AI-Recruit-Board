# Generated by Django 3.1.7 on 2021-10-17 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='show_description',
            new_name='short_description',
        ),
    ]