# Generated by Django 4.2.3 on 2023-07-07 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spiderapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingroom',
            name='booking_duration',
        ),
        migrations.AddField(
            model_name='meetingroom',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetingroom',
            name='sstart_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='meeting_rooms', to='spiderapp.employee'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='reserved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserved_rooms', to='spiderapp.employee'),
        ),
    ]