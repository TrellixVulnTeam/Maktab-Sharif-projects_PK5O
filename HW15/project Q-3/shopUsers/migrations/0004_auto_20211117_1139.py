# Generated by Django 3.2.9 on 2021-11-17 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopUsers', '0003_auto_20211117_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='emailtocustomer',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='emailtosupplier',
            old_name='order_item_id',
            new_name='order_item',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='supplier_id',
            new_name='supplier',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='user_id',
            new_name='user',
        ),
    ]
