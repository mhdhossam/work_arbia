# Generated by Django 5.1.1 on 2024-10-28 14:48

import django.db.models.deletion
import parler.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisement', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroslider',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hero_slider', to='product.category'),
        ),
        migrations.AddField(
            model_name='heroslidertranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='advertisement.heroslider'),
        ),
        migrations.AlterUniqueTogether(
            name='heroslidertranslation',
            unique_together={('language_code', 'master')},
        ),
    ]
