# Generated by Django 5.0 on 2024-12-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_generalinfo_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'company_services',
            },
        ),
    ]
