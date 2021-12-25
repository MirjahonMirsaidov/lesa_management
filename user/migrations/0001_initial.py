# Generated by Django 4.0 on 2021-12-25 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('additional_info', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Telefon raqam noto'g'ri.", regex='^(998)?\\d{9}\\Z')])),
            ],
        ),
    ]