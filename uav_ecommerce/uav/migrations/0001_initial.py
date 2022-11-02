# Generated by Django 3.2.7 on 2022-11-02 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('battery', models.CharField(max_length=50)),
                ('is_Active', models.BooleanField(default=True)),
                ('is_Home', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uav.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uav.category')),
            ],
        ),
    ]