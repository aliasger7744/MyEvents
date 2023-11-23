# Generated by Django 4.2.7 on 2023-11-21 07:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_members_status_alter_members_mid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evenetname', models.CharField(max_length=50)),
                ('eid', models.UUIDField(default=uuid.UUID('3cecb84b-83a9-4ae7-afe0-bd66ad181da4'), editable=False, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='members',
            name='mid',
            field=models.UUIDField(default=uuid.UUID('e5e9cb9e-9903-4194-8cad-b27f7bc9cefc'), editable=False, unique=True),
        ),
    ]