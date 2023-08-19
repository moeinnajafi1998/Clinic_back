# Generated by Django 4.2.3 on 2023-08-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
        ('registeration', '0002_requestgoods_alter_requestsession_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurse', models.CharField(max_length=30)),
                ('sick', models.CharField(max_length=30)),
                ('clinic', models.CharField(max_length=30)),
                ('typical_user', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('services', models.ManyToManyField(blank=True, to='registeration.service')),
                ('used_items', models.ManyToManyField(blank=True, to='managment.item')),
            ],
        ),
    ]