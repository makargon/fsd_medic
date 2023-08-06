# Generated by Django 4.2.1 on 2023-08-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
