# Generated by Django 4.1.5 on 2023-01-27 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_rename_order_like_product_alter_like_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='product',
        ),
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.comment', verbose_name='주문'),
            preserve_default=False,
        ),
    ]
