# Generated by Django 3.0.6 on 2020-06-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_auto_20200604_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(blank=True, upload_to='gram/'),
        ),
    ]
