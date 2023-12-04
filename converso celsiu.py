import PySimpleGUI as sg

# Função para converter Celsius para Fahrenheit
def cel_fah(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fah_cel(fahr):
    return (fahr - 32) * 5/9

# Criar o layout da janela
layout = [
    [sg.Text('Temperatura:'), sg.InputText(key='entrada')],
    [sg.Button('Celsius'), sg.Button('Fahrenheit')],
]

# Criar a janela
window = sg.Window('\t\t\t\t\t Conversor de Temperatura', layout)

while True:
    # Ler a janela
    event, values = window.read()

    # Se o evento for fechar a janela, encerrar o loop
    if event == sg.WIN_CLOSED:
        break

    # Se o evento for o botão 'Celsius'
    elif event == 'Celsius':
        try:
            # Obter o valor da entrada e converter para float
            celsius = float(values['entrada'])

            # Calcular Fahrenheit
            fahrenheit = cel_fah(celsius)

            # Exibir resultado
            sg.popup(f'{celsius} Celsius é igual a {fahrenheit} Fahrenheit')
        except ValueError:
            sg.popup('Insira um número válido para Celsius')

    # Se o evento for o botão 'Fahrenheit'
    elif event == 'Fahrenheit':
        try:
            # Obter o valor da entrada e converter para float
            fahrenheit = float(values['entrada'])

            # Calcular Celsius
            celsius = fah_cel(fahrenheit)

            # Exibir resultado
            sg.popup(f'{fahrenheit} Fahrenheit é igual a {celsius} Celsius')
        except ValueError:
            sg.popup('Insira um número válido para Fahrenheit')

# Fechar a janela ao finalizar
window.close()
