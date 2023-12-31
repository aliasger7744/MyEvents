# Generated by Django 4.2.7 on 2023-11-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_members_mid'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=50)),
                ('eid', models.UUIDField(editable=False)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('addeddate', models.DateField(auto_now=True)),
                ('addedtime', models.TimeField(auto_now=True)),
                ('payments', models.IntegerField(blank=True, null=True)),
                ('purchase', models.IntegerField(blank=True, null=True)),
                ('members', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
