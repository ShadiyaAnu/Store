# Generated by Django 5.0 on 2024-02-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0008_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]