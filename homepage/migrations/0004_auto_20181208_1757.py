# Generated by Django 2.1 on 2018-12-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='fax_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]
