# Generated by Django 4.1.7 on 2023-03-17 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_rename_user_bim_bmi_user_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='user_bmi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
