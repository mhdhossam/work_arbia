# Generated by Django 5.1.1 on 2024-11-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
    ]
