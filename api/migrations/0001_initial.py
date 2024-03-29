# Generated by Django 4.1.7 on 2023-03-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('platform', models.CharField(max_length=20)),
                ('year', models.SmallIntegerField(default=1970)),
                ('genre', models.CharField(max_length=127)),
                ('global_sales', models.FloatField()),
            ],
        ),
    ]
