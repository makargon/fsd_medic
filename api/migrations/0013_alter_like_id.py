# Generated by Django 4.2.4 on 2023-08-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_like_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]