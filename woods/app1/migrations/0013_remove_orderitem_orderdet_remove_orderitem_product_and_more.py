# Generated by Django 4.2.7 on 2024-01-16 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_order_orderitem_profile_delete_billing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='orderdet',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='orderitem',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
