# Generated by Django 4.1.5 on 2023-12-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('user', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
