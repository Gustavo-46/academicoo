# Generated by Django 5.2.1 on 2025-05-19 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliacao_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.avaliacaotipo', verbose_name='Tipo de Avaliação'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='area_saber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber', verbose_name='Área do Saber'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='instituicao_ensino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaoensino', verbose_name='Instituição de Ensino'),
        ),
        migrations.AlterField(
            model_name='cursodisciplina',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='cursodisciplina',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='area_saber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber', verbose_name='Área do Saber'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa'),
        ),
        migrations.AlterField(
            model_name='instituicaoensino',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='instituicao_ensino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaoensino', verbose_name='Instituição de Ensino'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='ocorrencia',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ocupacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao', verbose_name='Ocupação'),
        ),
    ]
