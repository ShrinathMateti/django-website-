# Generated by Django 4.2.3 on 2023-09-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_desc', models.CharField(max_length=200)),
                ('about_team', models.TextField(max_length=100)),
            ],
        ),
    ]