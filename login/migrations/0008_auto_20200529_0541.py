# Generated by Django 3.0.5 on 2020-05-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200529_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='apidata',
            name='email',
            field=models.EmailField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
