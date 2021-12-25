# Generated by Django 4.0 on 2021-12-25 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entered_person', to='auth.user'),
        ),
    ]
