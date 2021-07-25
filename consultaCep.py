import requests
import PySimpleGUI as sg


def consulta(cep):
    url = 'https://viacep.com.br/ws/'+str(cep)+'/json'
    response = requests.request('GET', url)
    content = response.json()
    return content

layout = [
    [sg.Text('Cep'), sg.Input(key='CepValue'), sg.Button('Consultar')],
    [sg.Output(size=(60,15))]
]
window = sg.Window('CEPs', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Consultar':
        res = consulta(values['CepValue'])
        if len(res) == 1:
          print('CEP Inválido.')
        else:  
          for key in res:
              print(key.upper(),':',res[key])
        print('------------------------------------------------------------------------------------')


