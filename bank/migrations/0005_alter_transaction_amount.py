# Generated by Django 4.1.7 on 2023-03-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_alter_account_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(editable=False, null=True),
        ),
    ]
