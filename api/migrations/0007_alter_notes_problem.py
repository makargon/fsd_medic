# Generated by Django 4.2.1 on 2023-07-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_lon_centers_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='problem',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Причина'),
        ),
    ]
