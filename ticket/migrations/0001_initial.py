# Generated by Django 4.2.8 on 2025-02-04 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ministerio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NivelServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField()),
                ('tiempo_respuesta', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_mail', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_fuente', models.CharField(choices=[('email', 'Email'), ('telefono', 'Teléfono'), ('sistema', 'Sistema Interno')], max_length=100)),
                ('tema_ayuda', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_vencimiento', models.DateField()),
                ('respuesta', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets_area', to='general.area')),
                ('asignado_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets_asignados', to=settings.AUTH_USER_MODEL)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.estadoticket')),
                ('nivel_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.nivelservicio')),
                ('usuario_ministerio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.ministerio')),
                ('usuario_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
