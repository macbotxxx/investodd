# Generated by Django 3.1.13 on 2021-09-25 01:23

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investment_plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Timestamp when the record was created.', max_length=20, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Modified date when the record was created.', max_length=20, verbose_name='Modified Date')),
                ('plan_name', models.CharField(blank=True, help_text='The investment name given to the plan available to be invested on', max_length=200, null=True, verbose_name='Investment Plan Name')),
                ('plan_percentage', models.PositiveIntegerField(blank=True, help_text='Investment plan percentage given to take action when the plan is activated.', null=True, verbose_name='Investment Plan Percentage')),
                ('minimum_amount', models.FloatField(blank=True, default=0, help_text='Investment plan minimum amount for the plan.', max_length=200, null=True, verbose_name='Plan Minimum Amount')),
                ('maximum_amount', models.FloatField(blank=True, default=0, help_text='Investment plan maximum amount for the plan.', max_length=200, null=True, verbose_name='Investment Plan Maximum Amount')),
                ('plan_usage_per_user', models.PositiveIntegerField(blank=True, help_text='Investment plan Usage was introduced to help and restrict users from reinvesting on the same investment plan, which after exceeding a particular duration the investor is instructed to invest on a new plan.', null=True, verbose_name='Investment Plan Usage Per User')),
                ('plan_duration', models.CharField(blank=True, choices=[('1', 'A Day Plan'), ('2', 'Two Days Plan'), ('3', 'Three Days Plan'), ('4', 'Four Days Plan'), ('5', 'Five Days Plan'), ('6', 'Six Days Plan'), ('7', 'A Full Week Plan'), ('14', 'Two Weeks Plan'), ('21', 'Three Weeks Plan'), ('28', 'A Month Plan'), ('56', 'Two Months Plan'), ('84', 'Three Month Plan'), ('112', 'Four Months Plan'), ('140', 'Five Months Plan'), ('168', 'Six Moonths Plan'), ('196', 'Seven Months Plan'), ('224', 'Eight Months Plan'), ('252', 'Nine Months Plan'), ('280', 'Ten Months Plan'), ('308', 'Eleven Months Plan'), ('336', 'A Year Plan')], help_text='Investment plan percentage given to take action when the plan is activated, NOTE-- the investment plan is meant to terminate after the duration which both the interest and capital will be added to the investor, INTEREST IS BEEN ADDED AFTER THE DURATION NOT HOURLY.', max_length=200, null=True, verbose_name='Investment Plan Percentage')),
            ],
            options={
                'verbose_name': 'Setup Investment Plan',
                'verbose_name_plural': 'Setup Investment Plan',
            },
        ),
    ]
