# Generated by Django 4.1.5 on 2023-06-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_activity_activity_tack_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=512)),
                ('b', models.CharField(max_length=512)),
                ('c', models.BooleanField(default=False)),
            ],
        ),
    ]