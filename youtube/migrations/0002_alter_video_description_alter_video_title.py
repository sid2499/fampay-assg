# Generated by Django 4.1.5 on 2023-01-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
