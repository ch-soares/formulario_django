from django.shortcuts import render, redirect
from paginapessoal.base.forms import CadastroForm


def formulario_validado_manualmente(request):
    ''' Formulário validado manualmente, sem o uso dos recursos do django forms'''

    dados = {}
    chaves = ['nome', 'email', 'idade', 'sexo', 'tecnologias', 'area_interesse', 'mensagem']
    campos_obrigatorios = {'nome', 'email', 'idade'}
    erros = {}
    for chave in chaves:
        valor = request.POST.getlist(chave)
        if chave == 'tecnologias':
            dados[chave] = valor
        elif len(valor) == 1:
            valor_extraido = valor[0]
            dados[chave] = valor_extraido
            if chave in campos_obrigatorios and valor_extraido == '':
                erros[chave] = f'O campo {chave} é obrigatório!'
        elif len(valor) == 0:
            dados[chave] = None
            if chave in campos_obrigatorios:
                erros[chave] = f'O campo {chave} é obrigatório!'
        else:
            raise ValueError('Alguém enviou dados em formato impróprio!')
    if erros:
        contexto = {'erros': erros, 'dados': dados}
        return render(request, 'base/formulario_sem_model_form.html', contexto)
    return render(request, 'base/formulario_sem_model_form.html', dados)


def formulario_model_form(request):
    ''' Formulário validado e com recursos do django forms'''

    if request == 'POST':
        form = CadastroForm(request.POST)
        if not form.is_valid():
            return render(request, 'base/formulario_model_form.html', {'form': form})
        redirect('https://www.google.com')
    form = CadastroForm()
    return render(request, 'base/formulario_model_form.html', {'form': form})
