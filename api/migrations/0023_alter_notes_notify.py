# Generated by Django 4.2.1 on 2023-07-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_notes_notify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notify',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время уведомления о записи'),
        ),
    ]
