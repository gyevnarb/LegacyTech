# Generated by Django 2.1.2 on 2018-10-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('will', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_names',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
    ]
