# Generated by Django 4.2.1 on 2023-07-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_user_disease_user_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='disease',
            field=models.ManyToManyField(blank=True, to='api.disease', verbose_name='Заболевание'),
        ),
    ]