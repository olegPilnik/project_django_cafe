# Generated by Django 4.2.2 on 2023-06-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_contact_open_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=30, unique=True)),
                ('twitter', models.CharField(blank=True, max_length=30)),
                ('facebook', models.CharField(blank=True, max_length=30)),
                ('instagram', models.CharField(blank=True, max_length=30)),
                ('telegram', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Chefs',
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Gallery'},
        ),
    ]
