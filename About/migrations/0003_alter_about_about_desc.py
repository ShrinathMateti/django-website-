# Generated by Django 4.2.3 on 2023-09-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0002_alter_about_about_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_desc',
            field=models.CharField(max_length=300),
        ),
    ]
