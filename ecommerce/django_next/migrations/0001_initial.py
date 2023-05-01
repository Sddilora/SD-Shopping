# Generated by Django 4.2 on 2023-04-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('category', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brand', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('num_reviews', models.IntegerField()),
                ('count_in_stock', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
