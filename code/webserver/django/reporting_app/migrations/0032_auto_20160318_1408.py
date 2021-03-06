# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-18 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting_app', '0031_auto_20160227_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileflow',
            name='cid',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'CID'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='ecgi',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'ECGI'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='gtp_connection_status',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'GTP connection status'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='gtp_protocol_type',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'GTP protocol type'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='gtp_tunnel_status',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'GTP tunnel status'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='gtp_version',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'GTP version'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='http_header',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'HTTP header'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='imei',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'IMEI'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='imsi',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'IMSI'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='ip_protocol_type',
            field=models.CharField(blank=True, default='unknown', max_length=64, verbose_name=b'IP protocol type'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='ip_version',
            field=models.CharField(blank=True, default='unknown', max_length=64, verbose_name=b'IP version'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='lac',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'LAC'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='mcc',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'MCC'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='mnc',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'MNC'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='msisdn',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'MSISDN'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='num_L7_bytes_received',
            field=models.IntegerField(default=0, verbose_name=b'Num L7 bytes received'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='num_L7_bytes_transmitted',
            field=models.IntegerField(default=0, verbose_name=b'Num L7 bytes transmitted'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='num_gtp_echo_failures',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Num GTP echo failures'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='num_http_errors',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Num HTTP errors'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='num_tunneled_L7_bytes_received',
            field=models.IntegerField(default=0, verbose_name=b'Num tunneled L7 bytes received'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='other_endpoint_ip_address',
            field=models.CharField(blank=True, default='unknown', max_length=64, verbose_name=b'Other endpoint IP address'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='rac',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'RAC'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='sac',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'SAC'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='tac',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'TAC'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='tunnel_id',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'Tunnel ID'),
        ),
        migrations.AlterField(
            model_name='mobileflow',
            name='vlan_id',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name=b'VLAN ID'),
        ),
    ]
