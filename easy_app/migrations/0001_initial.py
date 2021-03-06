# Generated by Django 3.2.6 on 2022-05-09 03:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('main_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('departmentname', models.CharField(max_length=30)),
                ('deaprtmentnumber', models.IntegerField()),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.CreateModel(
            name='DepartmentType',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('department_type', models.CharField(max_length=30)),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('shiftname', models.CharField(max_length=20)),
                ('shiftcode', models.CharField(max_length=4)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('empnumber', models.IntegerField(default=None, null=True)),
                ('contactnumber', models.IntegerField(default=None, null=True)),
                ('usertype', models.CharField(choices=[(1, 'Admin'), (2, 'Supervisor'), (3, 'Expert'), (4, 'Operator')], default=1, max_length=12)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('user_designation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('user_designation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('operationname', models.CharField(max_length=30)),
                ('operationdepartment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='easy_app.department')),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('machinename', models.CharField(max_length=30)),
                ('machinenumber', models.IntegerField(unique=True)),
                ('machinedescription', models.TextField()),
                ('machineoperation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='easy_app.operation')),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('user_designation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.AddField(
            model_name='department',
            name='deaprtmenttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='easy_app.departmenttype'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='easy_app.basemodel')),
                ('user_designation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('easy_app.basemodel',),
        ),
        migrations.AddField(
            model_name='user',
            name='userdepartment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='easy_app.department'),
        ),
    ]
