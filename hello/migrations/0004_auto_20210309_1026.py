# Generated by Django 3.1.6 on 2021-03-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20210302_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['due_date']},
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2021-03-09'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2021-03-09'),
        ),
    ]
