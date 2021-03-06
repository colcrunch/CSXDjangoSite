# Generated by Django 2.2.9 on 2020-02-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200129_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='coordinator_email',
            field=models.EmailField(default='csutherl@bhcc.edu', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_approved',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
