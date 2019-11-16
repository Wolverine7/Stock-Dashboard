# Generated by Django 2.2.6 on 2019-11-16 08:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(max_length=10)),
                ('to_currency', models.CharField(max_length=10)),
                ('from_number', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cust_FName', models.CharField(max_length=50)),
                ('cust_LName', models.CharField(max_length=50)),
                ('phoneNo', models.IntegerField()),
                ('cust_ssn', models.IntegerField()),
                ('cust_address1', models.CharField(max_length=300)),
                ('cust_address2', models.CharField(blank=True, max_length=100)),
                ('cust_country', models.CharField(max_length=100)),
                ('cust_zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('emp_FName', models.CharField(max_length=100)),
                ('emp_LName', models.CharField(max_length=100)),
                ('phoneNo', models.IntegerField()),
                ('emp_ssn', models.IntegerField()),
                ('emp_address1', models.CharField(max_length=300)),
                ('emp_address2', models.CharField(blank=True, max_length=100)),
                ('emp_country', models.CharField(max_length=100)),
                ('emp_zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('symbol', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('stock_fullname', models.CharField(max_length=30)),
                ('stock_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recent_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recent_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('watchlist_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='portfolio.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='watchListStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField(default=django.utils.timezone.now)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='portfolio.Stock')),
                ('watchList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.WatchList')),
            ],
        ),
    ]
