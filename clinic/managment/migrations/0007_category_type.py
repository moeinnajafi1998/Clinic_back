# Generated by Django 4.2.3 on 2023-08-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0006_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(blank=True, choices=[('Professional', 'P'), ('General', 'G')], max_length=12, null=True),
        ),
    ]
