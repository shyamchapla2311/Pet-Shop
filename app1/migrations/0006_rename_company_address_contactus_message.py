# Generated by Django 4.1.2 on 2023-02-04 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_contactus_subject_alter_contactus_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='company_address',
            new_name='message',
        ),
    ]