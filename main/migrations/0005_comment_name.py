# Generated by Django 5.1.3 on 2024-12-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='익명', max_length=100),
        ),
    ]
