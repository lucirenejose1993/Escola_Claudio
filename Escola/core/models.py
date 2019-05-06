from django.db import models

class User(models.Model):
	login = models.CharField("Login", max_length=15)
	senha = models.CharField("Senha", max_length=12)
	email = models.CharField("E-mail", max_length=50)
	def __str__(self):
		return self.email

class Aluno(models.Model):
	NomeCompA = models.CharField("Nome do Aluno", max_length=50)
	emailPersoA = models.CharField("E-mail", max_length=50)
	senhaA = models.CharField("Senha", max_length=12)
	def __str__(self):
		return self.NomeCompA


class Professor(models.Model):
	NomeCompP = models.CharField("Nome do professor", max_length=50)
	emailPersoP = models.CharField("E-mail", max_length=50)
	senhaP = models.CharField("Senha", max_length=12)
	DisciLec = models.CharField("Disciplinas Lecionadas", max_length=50)
	
	def __str__(self):
		return self.NomeCompP


class Disciplina(models.Model):
	NomeDisc = models.CharField("Disciplina", max_length=50)
	CargaH = models.IntegerField("Carga Horária", max_length=50)
	emailPersoP = models.CharField("E-mail", max_length=50)
	NomeCurs = models.CharField("Nome do Curso", max_length=50)
	
	def __str__(self):
		return self.NomeDisc	


