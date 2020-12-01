# Generated by Django 3.1.3 on 2020-11-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapi', '0003_auto_20201124_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banklone',
            old_name='status',
            new_name='Loan_Status',
        ),
        migrations.RemoveField(
            model_name='banklone',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='banklone',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='banklone',
            name='ApplicantIncome',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='banklone',
            name='CoapplicantIncome',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='banklone',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='banklone',
            name='Married',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True),
        ),
    ]
