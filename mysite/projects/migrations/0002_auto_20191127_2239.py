# Generated by Django 2.1.14 on 2019-11-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='coordinator',
            field=models.CharField(default='coordinator', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
