# Generated by Django 2.2 on 2020-05-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
