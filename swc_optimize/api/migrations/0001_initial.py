# Generated by Django 5.1.2 on 2024-10-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rune',
            fields=[
                ('rune_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('wizard_id', models.BigIntegerField()),
                ('occupied_type', models.IntegerField()),
                ('occupied_id', models.BigIntegerField()),
                ('slot_no', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('rune_class', models.IntegerField()),
                ('set_id', models.IntegerField()),
                ('upgrade_limit', models.IntegerField()),
                ('upgrade_curr', models.IntegerField()),
                ('base_value', models.IntegerField()),
                ('sell_value', models.IntegerField()),
                ('pri_eff', models.JSONField()),
                ('prefix_eff', models.JSONField()),
                ('sec_eff', models.JSONField()),
                ('extra', models.IntegerField()),
            ],
        ),
    ]
