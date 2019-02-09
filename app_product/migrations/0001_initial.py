# Generated by Django 2.0.8 on 2019-01-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('type', models.CharField(choices=[('tv.', 'Tv'), ('screen', 'Screen')], max_length=10)),
            ],
        ),
    ]