# Generated by Django 4.1.2 on 2023-02-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorregister',
            name='vendorimage',
            field=models.ImageField(default=None, upload_to='Vendor'),
        ),
    ]
