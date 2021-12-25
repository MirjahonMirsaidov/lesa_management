# Generated by Django 4.0 on 2021-12-25 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_alter_rent_entered_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.type'),
        ),
        migrations.AlterField(
            model_name='renteditem',
            name='record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rented_item', to='rent.rent'),
        ),
    ]