# Generated by Django 3.1.4 on 2020-12-20 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_project_projectimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.TextField(help_text='Long description of project', max_length=1000),
        ),
    ]
