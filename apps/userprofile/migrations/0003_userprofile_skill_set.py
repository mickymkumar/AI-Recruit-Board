# Generated by Django 3.1.7 on 2021-10-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_conversationmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='skill_set',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('AWS', 'AWS'), ('Azure', 'Azure')], max_length=100, null=True),
        ),
    ]