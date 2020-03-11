# Generated by Django 2.2 on 2020-02-19 15:32

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
            name='Dropdown_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Activity',
            },
        ),
        migrations.CreateModel(
            name='Dropdown_by_root_cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_cause', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Root Cause category',
            },
        ),
        migrations.CreateModel(
            name='Dropdown_Category_root_cause_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_tag', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Root Cause Tag',
            },
        ),
        migrations.CreateModel(
            name='Dropdown_loss_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loss_category', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Loss Category',
            },
        ),
        migrations.CreateModel(
            name='Dropdown_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Exception_By_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exception_type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Exception By Category',
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exception_Category', models.CharField(max_length=200)),
                ('Affiliate_Code', models.CharField(blank=True, max_length=5, null=True)),
                ('Affiliate_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Initiating_Branch', models.CharField(blank=True, max_length=200, null=True)),
                ('Zone', models.CharField(blank=True, max_length=20, null=True)),
                ('Region', models.CharField(blank=True, max_length=20, null=True)),
                ('Trn_Ref_no', models.CharField(blank=True, max_length=200, null=True)),
                ('Acccount_Number', models.CharField(blank=True, max_length=30, null=True)),
                ('Account_Name', models.CharField(max_length=200, null=True)),
                ('msisdn', models.CharField(blank=True, max_length=20, null=True)),
                ('ACCOUNT_CLASS', models.CharField(blank=True, max_length=10, null=True)),
                ('account_tier', models.IntegerField(blank=True, null=True)),
                ('DRCR_IND', models.CharField(blank=True, max_length=5, null=True)),
                ('ACY_CURR_BALANCE', models.FloatField(blank=True, default=0, null=True)),
                ('AC_OPEN_DATE', models.CharField(blank=True, max_length=50, null=True)),
                ('AcctPND', models.CharField(blank=True, max_length=3, null=True)),
                ('TnxCount', models.IntegerField(default=1, null=True)),
                ('DrMeanMaxAmt', models.IntegerField(blank=True, default=0, null=True)),
                ('CrMeanMaxAmt', models.IntegerField(blank=True, default=0, null=True)),
                ('Summary_Of_Incidence_and_CAMT_observation_during_Investigation', models.TextField(blank=True, max_length=100, null=True)),
                ('OPERATORS_RESPONSE', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_Discovered', models.CharField(blank=True, max_length=50, null=True)),
                ('Date_Regularised', models.DateTimeField(auto_now=True, null=True)),
                ('Currency', models.CharField(blank=True, max_length=5, null=True)),
                ('LCY_USD_RATE', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('Amount_Involved_LCY', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True)),
                ('Amount_at_Risk_LCY', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True)),
                ('Loss_prevented_LCY', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True)),
                ('Loss_prevented_USD', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True)),
                ('Inputter', models.CharField(blank=True, max_length=100, null=True)),
                ('Authoriser', models.CharField(blank=True, max_length=100, null=True)),
                ('USERID_Inputter', models.CharField(max_length=20, null=True)),
                ('USERID_Authoriser', models.CharField(max_length=20, null=True)),
                ('Month', models.CharField(blank=True, max_length=20, null=True)),
                ('Count2', models.IntegerField(blank=True, default=1, null=True)),
                ('ONBOARDING_DATE', models.CharField(blank=True, max_length=50, null=True)),
                ('statusCheck', models.CharField(blank=True, choices=[('Unreacted', 'Unreacted'), ('Pending', 'Pending'), ('Closed', 'Closed')], default='Unreacted', max_length=20, null=True)),
                ('camtDecision', models.CharField(blank=True, choices=[('Unreacted', 'Unreacted'), ('TruePositive', 'TruePositive'), ('FalsePositive', 'FalsePositive')], default='Unreacted', max_length=20, null=True)),
                ('Activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acl.Dropdown_activity')),
                ('CAMT_Reveiewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('Category_By_Root_Cause', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acl.Dropdown_by_root_cause')),
                ('Exception_By_Category_Type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acl.Exception_By_Category')),
                ('Loss_Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acl.Dropdown_loss_category')),
                ('Root_Cause_Tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acl.Dropdown_Category_root_cause_tag')),
                ('Status_REGULARIZED_UNREGULARIZED', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acl.Dropdown_status')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
