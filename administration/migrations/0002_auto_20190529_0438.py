# Generated by Django 2.2 on 2019-05-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
