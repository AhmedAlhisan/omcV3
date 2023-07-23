# Generated by Django 4.1.5 on 2023-05-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_activity_activity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_in_out',
            field=models.CharField(choices=[('inside', 'inside'), ('outside', 'outside')], default='inside', max_length=10),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_location',
            field=models.CharField(default='t', max_length=512),
            preserve_default=False,
        ),
    ]
