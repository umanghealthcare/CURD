# Generated by Django 4.0.6 on 2022-07-29 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(default='False', max_length=100),
        ),
    ]
