# Generated by Django 4.2.1 on 2023-07-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_notes_translate_remove_notes_translate_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='center',
        ),
        migrations.AddField(
            model_name='user',
            name='center',
            field=models.ManyToManyField(blank=True, null=True, to='api.centers', verbose_name='Центр'),
        ),
    ]