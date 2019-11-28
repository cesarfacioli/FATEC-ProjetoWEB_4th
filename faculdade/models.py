from django.db import models
from datetime import datetime

class Discente(models.Model):
    codmat = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, null=False, blank=False, default="", verbose_name="Aluno*", help_text="Nome completo do aluno, com no máximo de 120 caracteres.")

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    coddis = models.AutoField(primary_key=True)
    disciplina = models.CharField(max_length=50, null=False, blank=False, default="", verbose_name="Disciplina*", help_text="Nome da disciplina, com no máximo 50 caracteres.")

    def __str__(self):
        return self.disciplina


class Matricula(models.Model):
    ano = models.IntegerField()
    faltas = models.IntegerField()
    nota_final = models.FloatField()
    discente = models.ForeignKey(Discente, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.discente.nome

class Docente(models.Model):
    coddoc = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, null=False, blank=False, default="", verbose_name="Nome do Professor*", help_text="Nome completo do professor/docente, com no máximo 120 caracteres.")
    titulacao = models.CharField(max_length=50, null=False, blank=False, default="", verbose_name="Titulação*", help_text="Titulo do professor/docente, com no máximo 50 caracteres.")
    end_rua = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="Rua*", help_text="Nome da rua do professor/docente, com no máximo 100 caracteres.")
    end_numero = models.CharField(max_length=10, null=False, blank=False, default="", verbose_name="Número*", help_text="Número da moradia do professor/docente, com no máximo 10 caracteres.")
    end_bairro = models.CharField(max_length=50, null=False, blank=False, default="", verbose_name="Bairro*", help_text="Nome do bairro do professor/docente, com no máximo 50 caracteres.")
    end_cidade = models.CharField(max_length=50, null=False, blank=False, default="", verbose_name="Cidade*", help_text="Nome da cidade do professor/docente, com no máximo 50 caracteres.")
    end_complemento = models.CharField(max_length=50, default="Sem complemento", verbose_name="Complemento", help_text="Complemento da moradia do professor/docente, com no máximo 50 caracteres.")
    telefone = models.CharField(max_length=20, null=False, blank=False, default="(99) 99999-9999", verbose_name="Celular", help_text="Celular do professor/docente com máscara.")

    def __str__(self):
        return self.nome


class Alocacao(models.Model):
    ano_letivo = models.IntegerField()
    carga = models.IntegerField()
    horario = models.TimeField(auto_now=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.docente.nome
