# Generated by Django 4.1.5 on 2023-05-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_activity_activity_tack_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_tack_action',
            field=models.BooleanField(default=False),
        ),
    ]
