# Generated by Django 4.2.1 on 2023-07-24 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='center',
            new_name='centers',
        ),
        migrations.AddField(
            model_name='user',
            name='main_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='main_center', to='api.centers', verbose_name='Ведущий центр'),
        ),
    ]
