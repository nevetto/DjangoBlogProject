# Generated by Django 3.1.7 on 2022-08-15 19:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
