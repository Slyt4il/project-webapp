# Generated by Django 4.1.4 on 2022-12-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='media/profile_images/default.jpg', null=True, upload_to='media/profile_images/'),
        ),
    ]
