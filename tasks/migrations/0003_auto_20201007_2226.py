# Generated by Django 3.1.1 on 2020-10-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='info',
            field=models.IntegerField(),
        ),
    ]
