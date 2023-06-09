# Generated by Django 4.1.2 on 2023-02-01 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_vendorregister_vendorimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Category Name')),
                ('img', models.ImageField(upload_to='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorId', models.CharField(max_length=100)),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.IntegerField(default=0, max_length=5)),
                ('productDescription', models.TextField(default='')),
                ('productImage', models.ImageField(upload_to='product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product_category')),
            ],
        ),
    ]
