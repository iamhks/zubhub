# Generated by Django 3.2 on 2023-08-31 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_auto_20230831_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='materials_used',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
