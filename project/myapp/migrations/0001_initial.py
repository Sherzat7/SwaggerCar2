# Generated by Django 5.0.1 on 2024-02-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_ref', models.TextField()),
                ('product_title', models.TextField()),
                ('product_slug', models.TextField()),
                ('product_category', models.TextField()),
                ('product_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
