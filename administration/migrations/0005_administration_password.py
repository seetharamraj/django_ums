# Generated by Django 2.2 on 2019-05-29 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_auto_20190529_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='administration',
            name='password',
            field=models.CharField(default='Administration', max_length=20),
        ),
    ]
