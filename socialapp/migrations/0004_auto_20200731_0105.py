# Generated by Django 3.0.8 on 2020-07-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_auto_20200728_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
