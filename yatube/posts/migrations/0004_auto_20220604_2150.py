# Generated by Django 2.2.19 on 2022-06-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220604_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]
