# Generated by Django 3.2.19 on 2023-06-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_e2acuc', upload_to='images/'),
        ),
    ]