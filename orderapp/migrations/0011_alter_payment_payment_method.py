# Generated by Django 5.0 on 2024-02-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0010_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(default='None', max_length=100),
        ),
    ]