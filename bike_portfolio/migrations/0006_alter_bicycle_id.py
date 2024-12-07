# Generated by Django 5.1.3 on 2024-12-01 14:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_portfolio', '0005_alter_bicycle_description_alter_bicycle_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
