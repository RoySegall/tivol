# Generated by Django 2.2.6 on 2020-01-26 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentMigrationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=255)),
                ('destination_id', models.IntegerField()),
                ('model_target', models.CharField(max_length=255)),
            ],
        ),
    ]
