# Generated by Django 5.0.1 on 2024-01-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=30)),
                ('capital', models.CharField(max_length=30)),
            ],
        ),
    ]