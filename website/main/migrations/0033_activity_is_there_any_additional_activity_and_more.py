# Generated by Django 4.1.5 on 2023-09-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_employee_non_mulirty_classfication'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_there_any_additional_activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='the_additional_task',
            field=models.CharField(max_length=512, null=True),
        ),
    ]