# Generated by Django 5.1.1 on 2024-09-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
