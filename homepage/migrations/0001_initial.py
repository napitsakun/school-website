# Generated by Django 2.1 on 2018-12-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=100)),
                ('about_description', models.TextField()),
                ('about_image', models.FileField(upload_to='home-about/')),
            ],
        ),
        migrations.CreateModel(
            name='FacilitiesHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_image', models.FileField(upload_to='home-facility/')),
                ('facility_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SliderHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.FileField(upload_to='home-slider/')),
                ('slider_title', models.CharField(max_length=200, null=True)),
                ('slider_description', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
