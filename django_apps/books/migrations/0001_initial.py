# Generated by Django 4.1.6 on 2023-02-16 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
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
                ('updated', models.DateField(auto_now=True)),
                ('description', models.TextField()),
                ('room', models.IntegerField(blank=True, null=True)),
                ('bath', models.IntegerField(blank=True, null=True)),
                ('empty', models.BooleanField(default=False)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
