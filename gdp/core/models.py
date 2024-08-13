from django.db import models
from enum import Enum

class StatusProcesso(Enum):
    CIENTE = 'CIENTE'
    AVALIAR_PROC = 'AVALIAR PROC'
    HONORARIOS = 'HONORARIOS'
    HONORARIOS_ACEITO = 'HONORARIOS ACEITO'
    MARCAR_DATA = 'MARCAR DATA'
    DATA_ACEITA = 'DATA ACEITA'
    REALIZADO = 'REALIZADO'
    GERAR_LAUDO = 'GERAR LAUDO'
    LAUDO_ENVIADO = 'LAUDO ENVIADO'
    A_RECEBER_PAG = 'A RECEBER PAG'
    RECEBIDO_PAG = 'RECEBIDO PAG'


class Vara(models.Model):
    numero = models.CharField(max_length=10)
    comarca = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.numero} - {self.comarca}"


class TabelaPrecos(models.Model):
    tipo = models.CharField(max_length=50)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - R${self.valor_hora:.2f}/hora"


class Honorarios(models.Model):
    processo = models.ForeignKey('Processo', on_delete=models.CASCADE)
    procedimentos = models.TextField()
    horas_necessarias = models.DecimalField(max_digits=5, decimal_places=2)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Processo: {self.processo}, Valor Final: R${self.valor_final:.2f}"


class Processo(models.Model):
    vara = models.ForeignKey(Vara, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    data_recebimento = models.DateField()
    status = models.CharField(max_length=50, choices=[
        (status.value, status.name) for status in StatusProcesso])
    honorarios = models.OneToOneField('Honorarios', on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField()
    email = models.EmailField()
    link_processo = models.URLField()

    def __str__(self):
        return f"Processo {self.numero} - {self.vara.comarca}"
