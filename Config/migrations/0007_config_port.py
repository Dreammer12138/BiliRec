# Generated by Django 3.0.7 on 2020-08-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0006_auto_20200731_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='port',
            field=models.CharField(default='8000', max_length=8),
        ),
    ]
