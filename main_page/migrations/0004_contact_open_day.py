# Generated by Django 4.2.2 on 2023-06-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='open_day',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
