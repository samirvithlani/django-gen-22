# Generated by Django 4.1.2 on 2022-11-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]
