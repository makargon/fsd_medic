# Generated by Django 4.2.1 on 2023-07-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_user_disease_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='type_note',
        ),
        migrations.AddField(
            model_name='notes',
            name='online',
            field=models.BooleanField(default=False, verbose_name='Онлайн'),
        ),
    ]
