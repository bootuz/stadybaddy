# Generated by Django 3.0.7 on 2020-06-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('users', '0003_auto_20200609_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='announcements',
            field=models.ManyToManyField(blank=True, to='app.Announcement'),
        ),
    ]
