# Generated by Django 4.1.7 on 2023-03-10 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0009_alter_transaction_account_number_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='account_number_id',
            new_name='account_number',
        ),
    ]