# Generated by Django 3.2.19 on 2023-06-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../chef_el1rfp', upload_to='images/'),
        ),
    ]