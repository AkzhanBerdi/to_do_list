# Generated by Django 3.2 on 2023-05-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=25)),
                ('status', models.CharField(default='New', max_length=10)),
                ('dead_line', models.DateField(blank=True, default=None)),
            ],
        ),
    ]