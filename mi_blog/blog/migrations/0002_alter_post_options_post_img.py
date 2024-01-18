# Generated by Django 5.0.1 on 2024-01-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'записи'},
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
