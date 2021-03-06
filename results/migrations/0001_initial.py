# Generated by Django 2.2 on 2019-06-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roolno', models.CharField(max_length=10)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE')], max_length=50)),
                ('semister', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=50)),
                ('subjects', models.CharField(choices=[('M1', 'M1'), ('MM', 'MM'), ('CP', 'CP'), ('JAVA', 'JAVA'), ('DBMS', 'DBMS'), ('DS', 'DS'), ('OS', 'OS'), ('WP', 'WP')], max_length=50)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
