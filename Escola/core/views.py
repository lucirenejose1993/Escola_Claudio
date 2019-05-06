from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render (request, 'core/Home.html')

def disciplina(request):
    return render (request, 'core/Disciplinas.html')    

def lista_curso(request):
    return render (request, 'core/Lista de Curso.html')

def noticias(request):
    return render (request, 'core/Noticias.html')

def dm(request):
    return render (request, 'core/DM_ SQL.html')

def disciplina_1(request):
    return render (request, 'core/Disciplina_do_Curso1.html') 

def detalhe_1(request):
    return render (request, 'core/Detalhe_do_Curso1.html')

def detalhe_2(request):
    return render (request, 'core/Detalhe_do_Curso2.html')

def detalhe_3(request):
    return render (request, 'core/Detalhe_do_Curso3.html')

def detalhe_4(request):
    return render (request, 'core/Detalhe_do_Curso4.html')

def big_data(request):
    return render (request, 'core/ARQ_BI_BIG_DATA.html')

def data_w(request):
    return render (request, 'core/DATA_WAREHOUSING.html')

def comp_th(request):
    return render (request, 'core/COMPUTATIONAL_THINKING.html')

def data_a(request):
    return render (request, 'core/DATABASE_APPLICATION_DEVELOPMENT.html')

def admin_rede(request):
    return render (request, 'core/ADMINISTRAÇÃO_DE_REDES .html')

def conv_dig(request):
    return render (request, 'core/Convergência_Digital.html') 

def cenario(request):
    return render (request, 'core/Analise_Cenario_Economicos.html')

def marketing(request):
    return render (request, 'core/Conceitos_Práticas_de_Marketing.html')     