# Generated by Django 5.2.1 on 2025-05-19 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSaber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Área do Saber')),
            ],
            options={
                'verbose_name': 'Área do Saber',
                'verbose_name_plural': 'Áreas do Saber',
            },
        ),
        migrations.CreateModel(
            name='AvaliacaoTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Tipo de Avaliação')),
            ],
            options={
                'verbose_name': 'Tipo de Avaliação',
                'verbose_name_plural': 'Tipos de Avaliação',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Ocupação')),
            ],
            options={
                'verbose_name': 'Ocupação',
                'verbose_name_plural': 'Ocupações',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Turma')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Turno')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Curso')),
                ('carga_horaria_total', models.IntegerField(verbose_name='Carga Horária Total (horas)')),
                ('duracao_meses', models.IntegerField(verbose_name='Duração (meses)')),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Disciplina')),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='CursoDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horária')),
                ('periodo', models.IntegerField(verbose_name='Período')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
            options={
                'verbose_name': 'Disciplina por Curso',
                'verbose_name_plural': 'Disciplinas por Curso',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição da Avaliação')),
                ('avaliacao_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.avaliacaotipo')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.CreateModel(
            name='InstituicaoEnsino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Instituição')),
                ('site', models.CharField(max_length=100, verbose_name='Site')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
            options={
                'verbose_name': 'Instituição de Ensino',
                'verbose_name_plural': 'Instituições de Ensino',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao_ensino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaoensino'),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('pai', models.CharField(max_length=100, verbose_name='Nome do Pai')),
                ('mae', models.CharField(max_length=100, verbose_name='Nome da Mãe')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('dataNasc', models.DateField(verbose_name='Data de Nascimento')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição da Ocorrência')),
                ('data', models.DateField(verbose_name='Data da Ocorrência')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
            ],
            options={
                'verbose_name': 'Ocorrência',
                'verbose_name_plural': 'Ocorrências',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_previsao_termino', models.DateField(verbose_name='Previsão de Término')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('instituicao_ensino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaoensino')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
            ],
            options={
                'verbose_name': 'Matrícula',
                'verbose_name_plural': 'Matrículas',
            },
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_faltas', models.IntegerField(verbose_name='Número de Faltas')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
            ],
            options={
                'verbose_name': 'Frequência',
                'verbose_name_plural': 'Frequências',
            },
        ),
    ]
