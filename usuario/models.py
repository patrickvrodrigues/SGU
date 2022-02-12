from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    ativo =  models.BooleanField(default=True)

    class Meta:
        abstract = True


class Endereco(Base):
    endereco = models.CharField(max_length=255)
    uf = models.CharField(max_length=45)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=45)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255)
    cep = models.CharField(max_length=11)
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['id']

    def __str__(self):
        return self.endereco

class Polo(Base):
    SEDE = 1
    UR = 2
    ULSAV = 3
    EAC = 4
    BARREIRA = 5
    TIPO_POLO = (
        (1, 'Sede'),
        (2, 'UR'),
        (3, 'ULSAV'),
        (4, 'EAC'),
        (5, 'Barreira')
    )


    polo = models.CharField(max_length=100)
    tipo = models.PositiveSmallIntegerField(choices = TIPO_POLO)
    endereco = models.OneToOneField(Endereco, verbose_name='fk_endereco', on_delete=models.SET_NULL, null=True)
    subordinado = models.ForeignKey("Polo", related_name = 'subpolo', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Polo'
        verbose_name_plural = 'Polos'
        ordering = ['id']

    def __str__(self):
        return self.polo

class Pasta(Base):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Pasta'
        verbose_name_plural = 'Pastas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Setor(Base):
    setor = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255, blank=True)
    sigla = models.CharField(max_length=100, blank=True)
    polo = models.ForeignKey(Polo, on_delete=models.CASCADE)
    subordinado = models.ForeignKey("Setor", related_name = 'subsetor',on_delete=models.SET_NULL, null=True, blank=True)
    pasta = models.ForeignKey("Pasta", default=None, null = True, on_delete = models.SET_NULL, blank= True)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['pasta']

    def __str__(self):
        return self.setor




class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    setor = models.ForeignKey(Setor,related_name="usuarios",null = True, on_delete = models.SET_NULL, blank = True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return str(self.usuario)

