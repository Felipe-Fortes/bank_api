# Generated by Django 5.0.4 on 2024-04-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='compensation_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
