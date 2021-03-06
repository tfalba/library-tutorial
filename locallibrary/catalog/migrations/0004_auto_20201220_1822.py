# Generated by Django 3.1.4 on 2020-12-20 18:22

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='book',
            name='word',
            field=models.CharField(default=catalog.models.word_default, max_length=25),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='word',
            field=models.CharField(default=catalog.models.word_default, max_length=25),
        ),
    ]
