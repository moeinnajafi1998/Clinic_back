# Generated by Django 4.2.3 on 2023-08-05 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0003_clinic'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhareHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment.clinic', to_field='name')),
            ],
        ),
    ]