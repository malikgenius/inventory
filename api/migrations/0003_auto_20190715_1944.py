# Generated by Django 2.2.3 on 2019-07-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='kind',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]
