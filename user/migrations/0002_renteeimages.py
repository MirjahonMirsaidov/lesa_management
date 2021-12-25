# Generated by Django 4.0 on 2021-12-25 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenteeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('rentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.rentee')),
            ],
        ),
    ]