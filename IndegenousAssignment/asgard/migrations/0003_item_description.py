# Generated by Django 4.1.1 on 2022-09-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asgard', '0002_rename_asgard_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
