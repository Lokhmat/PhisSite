# Generated by Django 2.1.5 on 2019-03-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20190302_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='zadachi',
            name='answer',
            field=models.CharField(default=123, max_length=150),
            preserve_default=False,
        ),
    ]