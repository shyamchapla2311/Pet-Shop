# Generated by Django 4.1.2 on 2023-02-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_product_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('name', models.CharField(default='', max_length=20, verbose_name=' Subject')),
                ('company_address', models.TextField()),
            ],
        ),
    ]