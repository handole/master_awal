# Generated by Django 2.1.3 on 2018-11-16 08:31

import apps.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdakun', models.CharField(max_length=6, verbose_name='Kode akun')),
                ('nmakun', models.CharField(max_length=100, verbose_name='Nama akun')),
                ('kdjenbel', models.CharField(max_length=2, verbose_name='Kode Jenis Beli')),
                ('tahun', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=apps.models.current_year, verbose_name='Tahun')),
            ],
        ),
        migrations.CreateModel(
            name='Bulan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdbulan', models.CharField(max_length=2, verbose_name='Kode bulan')),
                ('nmbulan', models.CharField(max_length=15, verbose_name='Nama Bulan')),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kddept', models.CharField(max_length=3, verbose_name='Kode Dept')),
                ('nmdept', models.CharField(max_length=70, verbose_name='Nama Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Fungsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdfungsi', models.CharField(max_length=2, verbose_name='Kode Fungsi')),
                ('nmfungsi', models.CharField(max_length=30, verbose_name='Nama Fungsi')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='apps.Fungsi', verbose_name='Kode SFungsi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Giat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdgiat', models.CharField(max_length=4, verbose_name='Kode Giat')),
                ('nmgiat', models.CharField(max_length=70, verbose_name='Nama Giat')),
                ('versi', models.CharField(max_length=25, verbose_name='Versi')),
                ('tahun', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=apps.models.current_year, verbose_name='Tahun Giat')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('kdfungsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Fungsi', verbose_name='Kode Fungsi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kotam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdkotama', models.CharField(max_length=255, verbose_name='Kode Kotama')),
                ('nmkotama', models.CharField(max_length=255, verbose_name='Nama Kotama')),
                ('kdkukotama', models.CharField(max_length=255, verbose_name='Kode Kukotama')),
                ('kddept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kotam_dept', to='apps.Dept', verbose_name='Kode Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdoutput', models.CharField(max_length=3, verbose_name='Kode Output')),
                ('nmoutput', models.CharField(max_length=75, verbose_name='Nama Output')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('kdfungsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Fungsi', verbose_name='Output')),
                ('kdgiat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Giat', verbose_name='Kode Giat')),
                ('kdoutput1', mptt.fields.TreeForeignKey(max_length=2, on_delete=django.db.models.deletion.CASCADE, to='apps.Output', verbose_name='Kode Output 1')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdprogram', models.CharField(max_length=2, verbose_name='Kode Program')),
                ('nmprogram', models.CharField(max_length=45, verbose_name='Nama Program')),
                ('tahun', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=apps.models.current_year, verbose_name='Tahun Program')),
                ('versi', models.CharField(max_length=20, verbose_name='Versi')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('kdfungsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Fungsi', verbose_name='Kode Fungsi')),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prog_child', to='apps.Fungsi', verbose_name='Kode SFungsi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Satkr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdsatkr', models.CharField(max_length=2, verbose_name='Kode Satuan Kerja')),
                ('nmsatkr', models.CharField(max_length=80, verbose_name='Nama Satuan Kerja')),
                ('kddept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Dept', verbose_name='Kode Dept')),
                ('kdkotama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Kotam', verbose_name='Kode Kotama')),
            ],
        ),
        migrations.CreateModel(
            name='Satkun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdsakun', models.IntegerField(null=True, verbose_name='Kode Satuan Kunjungan')),
                ('nmsakun', models.CharField(max_length=255, verbose_name='Nama Satuan Kunjungan')),
                ('kddipa', models.CharField(max_length=1, verbose_name='Kode Dipa')),
                ('kdakun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='satkun_akun', to='apps.Akun', verbose_name='Kode Akun')),
                ('kdgiat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='satkun_giat', to='apps.Giat', verbose_name='Kode Giat')),
                ('kdoutput', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='satkun_output', to='apps.Output', verbose_name='Kode Output')),
            ],
        ),
        migrations.CreateModel(
            name='Subsatkr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdsubsatkr', models.CharField(max_length=2, verbose_name='Kode Sub SatKer')),
                ('nmsubsatkr', models.CharField(max_length=100, verbose_name='Nama SubSatkr')),
                ('kddept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Dept', verbose_name='Kode Dept')),
                ('kdkotama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Kotam', verbose_name='Kode Kotama')),
                ('kdsatkr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Satkr', verbose_name='Kode Satuan Kerja')),
            ],
        ),
        migrations.CreateModel(
            name='Tingkat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdtingkat', models.IntegerField(null=True)),
                ('pengguna', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdunit', models.IntegerField(null=True, verbose_name='Kode Unit')),
                ('nmunit', models.CharField(max_length=60, verbose_name='Nama Unit')),
                ('kddept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Dept', verbose_name='Kode Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Wasgiat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kdwasgiat', models.CharField(max_length=2, verbose_name='Kode Wasgiat')),
                ('nmwasgiat', models.CharField(max_length=30, verbose_name='Nama Wasgiat')),
            ],
        ),
        migrations.AddField(
            model_name='tingkat',
            name='kdwasgiat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Wasgiat'),
        ),
        migrations.AddField(
            model_name='subsatkr',
            name='kdunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Unit', verbose_name='Kode Unit'),
        ),
        migrations.AddField(
            model_name='satkr',
            name='kdkusatker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Satkun', verbose_name='Kode Kusatuan Kerja'),
        ),
        migrations.AddField(
            model_name='satkr',
            name='kdunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Unit', verbose_name='Kode Unit'),
        ),
        migrations.AddField(
            model_name='output',
            name='kdprogram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Program', verbose_name='Kode Program'),
        ),
        migrations.AddField(
            model_name='output',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='out_child', to='apps.Fungsi', verbose_name='Kode Sfungsi'),
        ),
        migrations.AddField(
            model_name='kotam',
            name='kdunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kotam_unit', to='apps.Unit', verbose_name='Kode Unit'),
        ),
        migrations.AddField(
            model_name='giat',
            name='kdprogram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Program', verbose_name='Kode Program'),
        ),
        migrations.AddField(
            model_name='giat',
            name='parent',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giat_child', to='apps.Fungsi', verbose_name='Kode SFungsi'),
        ),
    ]
