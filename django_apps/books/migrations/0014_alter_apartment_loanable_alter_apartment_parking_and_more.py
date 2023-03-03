# Generated by Django 4.1.6 on 2023-03-02 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_apartment_loanable_alter_apartment_parking_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='loanable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='parking',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='loanable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='parking',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='officetel',
            name='loanable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='officetel',
            name='parking',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='loanable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='parking',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='loanable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='parking',
            field=models.BooleanField(default=True),
        ),
    ]