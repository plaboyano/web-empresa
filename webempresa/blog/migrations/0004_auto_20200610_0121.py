# Generated by Django 2.1.15 on 2020-06-10 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200606_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.Category', verbose_name='categorias'),
        ),
    ]
