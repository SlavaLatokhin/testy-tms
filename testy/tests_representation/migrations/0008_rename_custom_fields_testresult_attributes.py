# Generated by Django 3.2.4 on 2023-01-11 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests_representation', '0007_testresult_custom_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testresult',
            old_name='custom_fields',
            new_name='attributes',
        ),
    ]
