# Generated by Django 3.0.7 on 2020-06-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
