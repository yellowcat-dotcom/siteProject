# Generated by Django 4.2.3 on 2023-07-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingparticipant',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]