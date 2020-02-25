from django.shortcuts import render
import requests


def mainpage(request):
    return render(request, 'core/mainpage.html')


def cep(request):
    cepid = request.GET.get('cep')
    res = {}
    if cepid:
        res = requests.get(f'https://viacep.com.br/ws/{cepid}/json/').json()
        print(res)

    return render(request, 'core/cep.html', {'resultado': res})


def cidadesufs(request):
    filteruf = request.GET.get('filteruf')
    filtercidade = request.GET.get('filtercidade')

    requf = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
    listaufs = requf.json()

    if type(filteruf) is str:
        filteruf = int(filteruf)
    if type(filtercidade) is str:
        filtercidade = int(filtercidade)

    ufatual = {}
    listacidadesfiltro = listacidadesdetalhe = []
    if filteruf:
        if filteruf != 0:
            reqcidade = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{filteruf}/'
                                     f'municipios')
            listacidadesfiltro = listacidadesdetalhe = reqcidade.json()
            ufatual = list(filter(lambda uf: uf["id"] == filteruf, listaufs))[0]
    if filtercidade:
        if filtercidade != 0:
            listacidadesdetalhe = list(filter(lambda cidade: cidade["id"] == filtercidade, listacidadesfiltro))
            print(listacidadesdetalhe)

    return render(request, 'core/cidadesufs.html', {'listaufs': listaufs, 'ufatual': ufatual,
                                                    'listacidadesfiltro': listacidadesfiltro,
                                                    'filtercidadeatual': filtercidade,
                                                    'listacidadesdetalhe': listacidadesdetalhe})


def filmes(request):
    filterano = request.GET.get('ano')

    qtdefilmes = 0
    resultado = []
    if filterano:
        req = requests.get(f'http://127.0.0.1:8080/yearmovies/{filterano}')
        resultado = req.json()
        qtdefilmes = len(resultado)

    return render(request, 'core/filmes.html', {'listafilmes': resultado, 'qtdefilmes': qtdefilmes})
