# Generated by Django 3.0.5 on 2020-05-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]