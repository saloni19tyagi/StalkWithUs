# Generated by Django 2.2.3 on 2020-04-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200412_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='codechef',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='codeforces',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='github',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='hackerearth',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='hackerrank',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='linkedin',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='spoj',
            field=models.TextField(blank=True, default=''),
        ),
    ]