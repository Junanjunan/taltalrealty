# Generated by Django 4.1.6 on 2023-02-16 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_realtor_account'),
        ('books', '0003_alter_apartment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='parking',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='pet',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('addres_detail', models.CharField(blank=True, max_length=30, null=True)),
                ('deal_type', models.CharField(choices=[('sell', 'sell'), ('lease', 'lease')], max_length=20)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('deposit', models.IntegerField(blank=True, null=True)),
                ('month_fee', models.IntegerField(blank=True, null=True)),
                ('management_fee', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('progress', 'progress'), ('finished', 'finished')], max_length=20)),
                ('owner', models.CharField(blank=True, max_length=100, null=True)),
                ('owner_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('on_lease', models.BooleanField(default=False)),
                ('loanable', models.BooleanField(default=True)),
                ('area_ex', models.FloatField(blank=True, null=True)),
                ('area_su', models.FloatField(blank=True, null=True)),
                ('area_land', models.FloatField(blank=True, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('elevator', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=True)),
                ('updated', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('room', models.IntegerField(blank=True, null=True)),
                ('bath', models.IntegerField(blank=True, null=True)),
                ('pet', models.BooleanField(default=False)),
                ('empty', models.BooleanField(default=False)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.realtor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]