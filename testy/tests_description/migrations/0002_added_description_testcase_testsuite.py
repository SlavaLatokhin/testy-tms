# Generated by Django 3.2.4 on 2022-12-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_description', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltestcase',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
        ),
        migrations.AddField(
            model_name='testsuite',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
        ),
    ]