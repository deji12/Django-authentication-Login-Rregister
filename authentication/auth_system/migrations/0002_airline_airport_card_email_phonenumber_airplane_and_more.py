# Generated by Django 5.0 on 2023-12-10 01:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('terminals', models.PositiveIntegerField()),
                ('airport_type', models.CharField(choices=[('domestic', 'Domestic'), ('international', 'International'), ('both', 'Both')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('name_on_card', models.CharField(max_length=128)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255, unique=True)),
                ('number_of_seats', models.PositiveIntegerField()),
                ('manufacturing_company', models.CharField(max_length=255)),
                ('model_number', models.CharField(max_length=255)),
                ('manufacturing_date', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_system.airline')),
            ],
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='cards',
            field=models.ManyToManyField(to='auth_system.card'),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='emails',
            field=models.ManyToManyField(to='auth_system.email'),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=255)),
                ('departure_datetime', models.DateTimeField()),
                ('arrival_datetime', models.DateTimeField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('on_time', 'On Time'), ('delayed', 'Delayed')], default='on_time', max_length=10)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_system.airline')),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_system.airplane')),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='auth_system.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='auth_system.airport')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceProcedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_system.airplane')),
            ],
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='phone_numbers',
            field=models.ManyToManyField(to='auth_system.phonenumber'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_number', models.IntegerField()),
                ('comment', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_system.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_datetime', models.DateTimeField()),
                ('passenger_first_name', models.CharField(max_length=128)),
                ('passenger_last_name', models.CharField(max_length=128)),
                ('passenger_date_of_birth', models.DateField()),
                ('credit_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_system.card')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_system.flight')),
            ],
        ),
    ]
