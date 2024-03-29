# Generated by Django 5.0.1 on 2024-02-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0007_alter_historicalinvoice_note_alter_invoice_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalinvoice',
            name='amount_due',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_due',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=20, null=True),
        ),
    ]
