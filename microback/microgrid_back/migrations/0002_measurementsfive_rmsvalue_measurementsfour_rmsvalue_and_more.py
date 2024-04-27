# Generated by Django 4.2.11 on 2024-04-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microgrid_back', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurementsfive',
            name='rmsvalue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurementsfour',
            name='rmsvalue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurementsone',
            name='rmsvalue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurementssix',
            name='rmsvalue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurementsthree',
            name='rmsvalue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurementstwo',
            name='rmsvalue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
