# Generated by Django 2.2 on 2021-12-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playdates_app', '0004_auto_20211209_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
