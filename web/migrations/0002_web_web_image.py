# Generated by Django 4.2.3 on 2023-09-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='web_image',
            field=models.FileField(default=None, max_length=255, null=True, upload_to='web/'),
        ),
    ]
