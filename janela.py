from tkinter.ttk import *
from tkinter import *
import pandas as pd
import webbrowser
from api import info_cliente



def seleciona_mascara(linha, coluna, num_contrato):
    planilha = pd.read_excel('Mascaras.xlsx', sheet_name='dadosst')
    
    dicio = {}
    texto_formatado = ''
    
    texto = planilha.iat[linha, coluna]

    linhas = texto.split('\n')

    for chave in linhas:
        if chave not in dicio:
            if chave == 'SINAL: ':
                dicio[chave] = info_cliente[f'{num_contrato}']['Luz']
            elif chave == 'MODELO e SN da ONU/Roteador:':
                dicio[chave] = info_cliente[f'{num_contrato}']['Modelo ONU/SN']
            elif chave == 'UPTIME: ':
                dicio[chave] = info_cliente[f'{num_contrato}']['Uptime']
            elif chave == 'TOPOLOGIA:':
                dicio[chave] = info_cliente[f'{num_contrato}']['Topologia']
            else:
                dicio[chave] = ''
                      
    for k, v in dicio.items():
        texto_formatado += f'{k} {v}"\n"'.replace('"', '')
    
    return txt_area.insert(END, texto_formatado)


def mostra_mascara_preenchida():
    mascara = cbx_mascara.get()
    contrato = input_num_contrato.get()
    txt_area.delete('1.0', END)
    if mascara == 'Sem conexão':
        seleciona_mascara(0,0,contrato)
    elif mascara == 'Lentidão/Oscilação':
        seleciona_mascara(0,1,contrato)
    elif mascara == 'Cobrança de OS':
        seleciona_mascara(0,2,contrato)
    elif mascara == 'Liberação de porta':
        seleciona_mascara(0,3,contrato)
    elif mascara == 'Troca de senha':
        seleciona_mascara(2,0,contrato)
    elif mascara == 'Teste de velocidade':
        seleciona_mascara(2,1,contrato)
    elif mascara == 'Upgrade':
        seleciona_mascara(2,3,contrato)

    link_ip.configure(text=f'{info_cliente[f"{contrato}"]["ip"]}', fg='blue', cursor='hand2')
    link_ip.bind('<Button-1>', lambda x: webbrowser.open_new(f'{info_cliente[f"{contrato}"]["ip"]}'))

def copiar():
    masc = txt_area.get('1.0', END)
    btn_copiar.clipboard_append(masc)

janela = Tk()
janela.title('Mascara suporte tecnico')
janela.geometry('400x600')
janela.resizable(0,0)

# Label
lbl_num_contrato = Label(janela, text='Número do contrato')
lbl_num_contrato.place(x=10, y=10)

#input
input_num_contrato = Entry(janela, width=32)
input_num_contrato.place(x=150, y=10)

#combobox
lbl_cbx = Label(janela, text='Tipo de máscara')
lbl_cbx.place(x=10, y=40)
mascaras = (
    'Sem conexão', 
    'Lentidão/Oscilação', 
    'Cobrança de OS', 
    'Liberação de porta', 
    'Troca de senha', 
    'Teste de velocidade', 
    'Upgrade'
)
cbx_mascara = Combobox(janela, values=mascaras, width=30)
cbx_mascara.place(x=151, y=40)

#link de ip
link_ip = Label(janela, text='')
link_ip.place(x=250, y=105)

lbl_ip = Label(janela, text='IP: ')
lbl_ip.place(x=230, y=105)


#Botões
btn_buscar = Button(janela, text='Buscar', command=mostra_mascara_preenchida)
btn_buscar.place(x=10, y=100)

btn_copiar = Button(janela, text='Copiar máscara', command=copiar)
btn_copiar.place(x=100, y=100)

# Area de texto
txt_area = Text(janela, width=56, height=20)
txt_area.place(x=0, y=150)



janela.mainloop()