# Generated by Django 4.1.4 on 2022-12-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twittapp', '0004_twitt_timestamp_alter_twitt_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitt',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
