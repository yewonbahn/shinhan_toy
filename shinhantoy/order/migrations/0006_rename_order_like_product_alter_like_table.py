# Generated by Django 4.1.5 on 2023-01-27 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_rename_product_like_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='order',
            new_name='product',
        ),
        migrations.AlterModelTable(
            name='like',
            table='shinhan_comment_like',
        ),
    ]
