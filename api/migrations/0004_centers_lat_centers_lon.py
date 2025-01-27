# Generated by Django 4.2.1 on 2023-07-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_notes_special_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='centers',
            name='lat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='centers',
            name='lon',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
