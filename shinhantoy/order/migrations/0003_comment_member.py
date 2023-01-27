# Generated by Django 4.1.5 on 2023-01-26 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자'),
            preserve_default=False,
        ),
    ]