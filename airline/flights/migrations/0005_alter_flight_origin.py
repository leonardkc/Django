# Generated by Django 3.2.9 on 2022-12-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20221208_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.TextField(default=''),
        ),
    ]
