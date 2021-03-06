# Generated by Django 2.1 on 2020-04-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200423_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_token',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
