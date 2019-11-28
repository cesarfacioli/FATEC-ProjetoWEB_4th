from django.contrib import admin
from .models import Disciplina, Discente, Docente, Matricula, Alocacao


@admin.register(Disciplina)
class admin_disciplina(admin.ModelAdmin):
    list_display = ['coddis', 'disciplina']


@admin.register(Discente)
class admin_aluno(admin.ModelAdmin):
    list_display = ['codmat', 'nome']


@admin.register(Docente)
class admin_professor(admin.ModelAdmin):
    list_display = ['coddoc', 'nome', 'end_cidade', 'end_bairro', 'end_rua', 'end_numero', 'end_complemento', 'telefone', 'titulacao']


@admin.register(Matricula)
class admin_matricula(admin.ModelAdmin):
    list_display = ['discente', 'disciplina', 'ano', 'faltas', 'nota_final']


@admin.register(Alocacao)
class admin_alocacao(admin.ModelAdmin):
    list_display = ['docente', 'disciplina', 'ano_letivo', 'carga', 'horario']


# admin.site.register(Discente)
# admin.site.register(Disciplina)
# admin.site.register(Docente)
# admin.site.register(Matricula)
# admin.site.register(Alocacao)