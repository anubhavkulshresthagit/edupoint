# Generated by Django 3.0.6 on 2020-07-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
    ]
