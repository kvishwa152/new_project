# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmployeeEmployeedetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=255)
    emp_salary = models.IntegerField()
    emp_email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'employee_employeedetails'


class Ipl(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    innings = models.IntegerField(blank=True, null=True)
    overs = models.IntegerField(blank=True, null=True)
    ballnumber = models.IntegerField(blank=True, null=True)
    batter = models.TextField(blank=True, null=True)
    bowler = models.TextField(blank=True, null=True)
    non_striker = models.TextField(db_column='non-striker', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    extra_type = models.TextField(blank=True, null=True)
    batsman_run = models.IntegerField(blank=True, null=True)
    extras_run = models.IntegerField(blank=True, null=True)
    total_run = models.IntegerField(blank=True, null=True)
    non_boundary = models.IntegerField(blank=True, null=True)
    iswicketdelivery = models.IntegerField(db_column='isWicketDelivery', blank=True, null=True)  # Field name made lowercase.
    player_out = models.TextField(blank=True, null=True)
    kind = models.TextField(blank=True, null=True)
    fielders_involved = models.TextField(blank=True, null=True)
    battingteam = models.TextField(db_column='BattingTeam', blank=True, null=True)  # Field name made lowercase.
    myunknowncolumn = models.TextField(db_column='MyUnknownColumn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ipl'


class Smartphones1(models.Model):
    brand_name = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    has_5g = models.TextField(blank=True, null=True)
    has_nfc = models.TextField(blank=True, null=True)
    has_ir_blaster = models.TextField(blank=True, null=True)
    processor_brand = models.TextField(blank=True, null=True)
    num_cores = models.IntegerField(blank=True, null=True)
    processor_speed = models.FloatField(blank=True, null=True)
    battery_capacity = models.IntegerField(blank=True, null=True)
    fast_charging_available = models.IntegerField(blank=True, null=True)
    fast_charging = models.TextField(blank=True, null=True)
    ram_capacity = models.IntegerField(blank=True, null=True)
    internal_memory = models.IntegerField(blank=True, null=True)
    screen_size = models.FloatField(blank=True, null=True)
    refresh_rate = models.IntegerField(blank=True, null=True)
    num_rear_cameras = models.IntegerField(blank=True, null=True)
    num_front_cameras = models.IntegerField(blank=True, null=True)
    os = models.TextField(blank=True, null=True)
    primary_camera_rear = models.IntegerField(blank=True, null=True)
    primary_camera_front = models.IntegerField(blank=True, null=True)
    extended_memory_available = models.IntegerField(blank=True, null=True)
    extended_upto = models.TextField(blank=True, null=True)
    resolution_width = models.IntegerField(blank=True, null=True)
    resolution_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smartphones1'
