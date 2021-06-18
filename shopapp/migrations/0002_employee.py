# Generated by Django 3.0.5 on 2021-06-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(unique=True)),
                ('fname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('salary', models.CharField(max_length=40)),
                ('phone_no', models.BigIntegerField(unique=True)),
            ],
            options={
                'db_table': 'employeeinfo',
            },
        ),
    ]
