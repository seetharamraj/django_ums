# Generated by Django 2.2 on 2019-05-29 05:26

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20190529_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
