# Generated by Django 2.1 on 2018-08-03 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_message_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.TextField(max_length=256, null=True),
        ),
    ]