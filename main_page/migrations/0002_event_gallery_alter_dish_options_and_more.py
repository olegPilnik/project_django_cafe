# Generated by Django 4.2.2 on 2023-06-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('count', models.SmallIntegerField()),
                ('event_name', models.CharField(max_length=50)),
                ('maneg', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('photo', models.ImageField(blank=True, upload_to='event/% Y/% m/% d/')),
            ],
            options={
                'verbose_name_plural': 'Events',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='gallery/% Y/% m/% d/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('category', 'position'), 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ('position',), 'verbose_name_plural': 'Dish Categories'},
        ),
    ]