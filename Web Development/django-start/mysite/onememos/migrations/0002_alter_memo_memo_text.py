# Generated by Django 5.1.4 on 2024-12-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onememos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='memo_text',
            field=models.CharField(max_length=250),
        ),
    ]
