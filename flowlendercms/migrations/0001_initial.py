# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 13:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_tittle', models.CharField(max_length=100)),
                ('deatil', models.TextField(max_length=500)),
                ('pdf_image', models.ImageField(blank=True, upload_to='flowlenders')),
                ('pdf_file', models.ImageField(blank=True, upload_to='flowlenders')),
            ],
        ),
        migrations.CreateModel(
            name='ClientDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('reffering_party', models.CharField(max_length=50)),
                ('data_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('ammount_request', models.DecimalField(decimal_places=2, max_digits=5)),
                ('debit_for', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_plan', models.CharField(choices=[('Weekly', 'Weekly'), ('Bi-Weekly', 'Bi-Weekly'), ('Monthly', 'Monthly')], default='Weekly', max_length=16)),
                ('credit_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('current_status', models.CharField(choices=[('Submitted', 'Submitted'), ('Funded', 'Funded'), ('Declined', 'Declined'), ('Waiting for Further Documents', 'Waiting for Further Documents')], default='Submitted', max_length=16)),
                ('contact_name', models.CharField(max_length=50)),
                ('mailing_address', models.TextField(default='NIL', max_length=200)),
                ('office_number', models.CharField(default='NIL', max_length=50)),
                ('mobile_number', models.CharField(default='NIL', max_length=50)),
                ('fax_number', models.CharField(default='NIL', max_length=50)),
                ('email', models.EmailField(default='def@def.def', max_length=254)),
                ('debit_ratio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_address', models.TextField(max_length=200)),
                ('office_number', models.CharField(max_length=50)),
                ('toll_number', models.CharField(max_length=50)),
                ('fax_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('data_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_tittle', models.CharField(max_length=100)),
                ('deatil', models.TextField(max_length=500)),
                ('pdf_image', models.ImageField(blank=True, upload_to='flowlenders')),
                ('pdf_file', models.ImageField(blank=True, upload_to='flowlenders')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_tittle', models.CharField(max_length=100)),
                ('deatil', models.TextField(max_length=500)),
                ('icon', models.ImageField(blank=True, upload_to='flowlenders')),
            ],
        ),
    ]
