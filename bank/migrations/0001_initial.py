# Generated by Django 4.1.7 on 2023-03-09 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=50, unique=True)),
                ('balance', models.FloatField()),
                ('customer_name', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updatd_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=50, unique=True)),
                ('amount', models.FloatField()),
                ('transaction_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updatd_at', models.DateTimeField(auto_now=True)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.account')),
            ],
        ),
    ]
