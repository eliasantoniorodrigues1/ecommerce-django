# Generated by Django 4.1.5 on 2023-01-27 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
