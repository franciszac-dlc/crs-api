# Generated by Django 2.0 on 2017-12-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('class_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course', models.CharField(blank=True, default='', max_length=20)),
                ('class_name', models.CharField(max_length=50)),
                ('credits', models.FloatField(default=0.0)),
                ('schedule', models.TextField()),
                ('instructor', models.CharField(max_length=50)),
                ('remarks', models.TextField()),
                ('slots_avail', models.IntegerField(default=0)),
                ('slots_total', models.IntegerField(default=0)),
                ('demand', models.IntegerField(default=0)),
            ],
        ),
    ]