# Generated by Django 4.2.7 on 2023-11-21 07:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_events_description_alter_events_eid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='eid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='mid',
            field=models.UUIDField(default=uuid.UUID('f0f76861-fed9-433b-8817-9f1ad8717f4e'), editable=False, unique=True),
        ),
    ]
