# Generated by Django 3.2.7 on 2022-11-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav', '0002_auto_20221103_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='uav',
            name='price',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
    ]
