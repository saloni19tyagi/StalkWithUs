# Generated by Django 3.0.5 on 2020-04-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200412_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='institute',
            field=models.TextField(blank=True, default=''),
        ),
    ]
