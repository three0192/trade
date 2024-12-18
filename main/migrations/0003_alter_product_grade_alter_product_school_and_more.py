# Generated by Django 5.1.3 on 2024-12-03 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_subject_product_photo_product_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='grade',
            field=models.CharField(choices=[('1', '1학년'), ('2', '2학년'), ('3', '3학년')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='school',
            field=models.CharField(choices=[('middle', '중학교'), ('high', '고등학교')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='subject',
            field=models.CharField(choices=[('korean', '국어'), ('english', '영어'), ('math', '수학'), ('history', '한국사'), ('social', '사회 탐구'), ('science', '과학 탐구')], max_length=20),
        ),
    ]
