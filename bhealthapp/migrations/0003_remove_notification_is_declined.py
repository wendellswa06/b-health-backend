# Generated by Django 3.2.12 on 2023-03-13 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bhealthapp', '0002_remove_result_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_declined',
        ),
    ]
