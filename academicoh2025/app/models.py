from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=11, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total (horas)")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    email = models.EmailField(verbose_name="Email")
    dataNasc = models.DateField(verbose_name="Data de Nascimento")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Previsão de Término")

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição da Avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class Turnos(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do Turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"


class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição da Ocorrência")
    data = models.DateField(verbose_name="Data da Ocorrência")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return f"{self.pessoa} - {self.data}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    periodo = models.IntegerField(verbose_name="Período")

    def __str__(self):
        return f"{self.curso} - {self.disciplina} ({self.periodo}º período)"

    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Curso"
