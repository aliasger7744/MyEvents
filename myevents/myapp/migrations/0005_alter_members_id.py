# Generated by Django 4.2.7 on 2023-11-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_members_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]