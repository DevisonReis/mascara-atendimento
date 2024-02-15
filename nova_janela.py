from tkinter import *
from tkinter.ttk import *
import webbrowser
from api import info_cliente


dicio_sac = {
    'Boleto': 
{'**BOLETO**': '',
'Detalhe: Cliente entrou em contato pelo plataforma chat/voz, solicitando boleto': '',

'Solução: Boleto referente a 14/04, enviado via e-mail-chat-whatsapp': '',
'Orientado o pagamento com pix e acesso a central do assinante': ''},
    'Desbloqueio': 
{'**DESBLOQUEIO**': '',
'Detalhe: Cliente entrou em contato solicitando o desbloqueio': '',

'Solução: Primeiro/Segundo desbloqueio. Comprovante recebido.': '',
'Ciente do prazo de 48h e que o segundo desbloqueio só será possível mediante envio do comprovante de pagamento.': '',
'Boleto referente ao vencimento 11/04 realizado': ''},
    'Duvida': 
{'**DÚVIDA**': '',
'Detalhe 1: Cliente entrou em contato para saber informações sobre o contrato': '',

'Detalhe 2: Cliente entrou em contato para saber sobre a visita técnica': '',

'Solução 1: Informado sobre o prazo da fidelidade, dia de vencimento do boleto e valor da mensalidade': '',

'Solução 2: Informado dia e perído (21/04/2023 no período da tarde) da realização da visita': ''},
    'Comprovante de pagamento': 
{'**COMPROVANTE DE PAGAMENTO**': '',
'Detalhe: Cliente enviou o comprovante de pagamento': '',

'Solução: Comprovante ref ao vencimento 14/04 recebido': ''},
    'Upgrade/Downgrade': 
{'**UPGRADE/DOWNGRADE**': '',
'Detalhe: Cliente solicitou alteração do seu plano': '',

'Solução: Contrato renovado para o plano de 300MB, pagando R$79,90.': '',
'Data de vencimento: 14 (de acordo com a solicitação)': '',
'Ciente da fidelidade': '',

'Obs.: Em caso de downgrade com renovação, cliente tem a isenção de multa.': '',
'A multa do downgrade, é a metade do valor da multa da rescisão contratual': ''},
    'Alteração do tipo de pagamento': 
{'**ALTERAÇÃO DO TIPO DE PAGAMENTO**': '',
'Detalhe: Cliente solicitou alteração do tipo de pagamento de cartão para boleto': '',

'Solução: Tipo de pagamento alterado.': '',
'Cliente ciente que a alteração só vai ocorrer no mês seguinte.': ''},
    'Suspensão de contrato/Ativação': 
{'**SUSPENSÃO DE CONTRATO/ATIVAÇÃO**': '',
'Detalhe 1: Cliente pediu a suspensão do contrato': '',

'Detalhe 2: Cliente com contrato cancelado, pede reativação': '',

'Solução 1: Informado que só poderá realizar a cada 12 meses': '',
'Ciente dos prazos (30, 60, 90 e 120 dias) e do proporcional de uso': '',
'Suspenso por 30 dias ': '',
'OBS: verificar se não tem pendências. Se tiver carnê lançado, abrir intervenção e solicitar estorno': '',

'Solução 2: Contrato reativado após baixa dos boletos negociados': '',
'OBS.: (fechar a o.s. de retirada de equipamento e vincular o equipamento no sistema)': '',
'Se o cliente não autenticar, enviado para o nível 2, pois o equipamento vai está desprovisionado.': ''},
    'SVA': 
{'**SVAs**': '',
'Detalhe: Cliente solicita a chave Deezer/HBO/LOOKE': '',

'Solução: Ciente do prazo e de como realizar o acesso.': '',
'Deezer: recebimento do SMS': '',
'LOOKE e HBO: Envio do e-mail com o manual': ''},
    'Indicação de amigo': 
{'**INDICAÇÃO DE AMIGO**': '',
'Detalhe: Cliente entrou em contato e solicitou o desconto indique um amigo': '',

'Solução: Amigo indicado: (Código do cliente, nome completo)': '',
'Instalado:': '',
'OBS.: abrir atendimento também do amigo indicado e informar o nome do amigo que indicou': ''},
    'Troca de titularidade': 
{'**TROCA DE TITULARIDADE**': '',

'Detalhe: Cliente solicitou troca de titularidade': '',

'Solução: Documentos anexados': '',
'Cliente do prazo de 72h úteis': '',
'Novo titular:': '',
'Telefone: ': '',
'E-mail:': ''},
    'Mudança de endereço': 
{'**MUDANÇA DE ENDEREÇO**': '',

'Detalhe: Cliente deseja realizar a mudança de endereço': '',
'Endereço Antigo: ': '',
'Endereço Novo: ': '',

'Solução: Solicitado que levasse o equipamento para o novo endereço': '',
'1ª ou 2ª Mudança': '',
'Ciente da taxa (74,95):': '',
'Telefone:': '',
'OBS: verificar se não tem pendências': ''},
    'Mudança de local': 
{'**MUDANÇA DE LOCAL**': '',

'Detalhe: Cliente deseja realizar a mudança de local ': '',

'Solução: Cliente deseja tirar o equipamento da sala e colocar no quarto': '',
'Ciente da taxa (R$99,90):': '',
'Telefone: ': ''},
    'Alteração de vencimento': 
{'**ALTERAÇÃO DO VENCIMENTO**': '',

'Detalhe: Cliente solicita alteração da data de vencimento.': '',

'Solução: Alterar o vencimento para nova data 07/10/14/25.': '',
'Cliente ciente que a alteração só vai ocorrer no mês seguinte.': ''},
    'Inversão de pagamento': 
{'**INVERSÃO DE PAGAMENTO**': '',

'Detalhe: Cliente pagou o boleto de Maio ao invés do de Abril': '',

'Solução: Realizar a inversão do pagamento.': '',
'Cliente ciente do prazo ': ''},
    'Estorno': 
{'**ESTORNO**': '',
'(Em casos de desconto sem conexão, informar os dias que o cliente perdeu o acesso e o mês de ref.)': '',

'Detalhe 1: Cliente informa que o boleto está divergente com o valor do contrato': '',

'Detalhe 2: Cliente informa que foi concedido o desconto no boleto, porém não foi aplicado.': '',

'Solução 1: Estornar boleto e corrigir o valor do contrato ': '',
'Está sendo cobrado R$149,90, quando deveria estar no valor de R$79,90 ': '',

'Solução 2: Estornar boleto do mês de Maio e corrigir com o valor com desconto ofertado de 50% ou referente a 5 dias sem conexão': '',
'vencimento 14/03/2023': '',
'valor: R$79,90': ''},
    'Nota fiscal': 
{'**NOTA FISCAL**': '',

'Detalhe: Cliente deseja a NF do mês de Maio': '',

'Solução: Verificado na central do assinante e não consta no sistema': '',
'e-mail:': '',
'Cliente ciente do prazo de 5 dias úteis para lançamento e envio da nota': ''},
    'Negociação': 
{'**NEGOCIAÇÃO**': '',

'Detalhe: Cliente entrou em contato solicitando negociação dos boletos em aberto (Permitido apenas para boletos a partir de 30 dias de atraso).': '',

'Solução: Negociar boletos com vencimentos: 14/02 e 14/03': '',
'Telefone: ': ''},
    'Duplicidade de pagamento': 
{'**DUPLICIDADE DE PAGAMENTO**': '',

'Detalhe: Cliente pagou duas vezes o boleto com vendimento 14/02': '',

'Solução 1: Comprovantes anexados no sistema': '',
'Cliente deseja que o próximo boleto seja liquidado.': '',

'Solução 2: Comprovantes anexados no sistema': '',
'Cliente deseja que o valor seja estornado': '',
'Nome Completo:': '',
'CPF:': '',
'Banco:': '',
'Conta:': '',
'Op.:': ''}
}

dicio_n1 = {
    'Sem conexão': {
        'SEM AUTENTICAÇÃO': '',
        'PROBLEMA': '',
        'SINAL:': '',
        'REDE WI-FI DISPONIVEL?': '',
        'REQUISIÇÃO DE AUTENTICAÇÃO:': '',
        'MODELO e SN da ONU:': '',
        'TOPOLOGIA:': '',
        'TELs DE CONTATO:': ''
    },
    'Lentidão/Oscilação': {
        'LENTIDÃO/OSCILAÇÃO': '',
        'PROBLEMA:': '',
        'via CABO ou WIFI:': '',
        'UPTIME:': '',
        'SINAL:': '',
        'DNS PADRÃO:': '',
        'MODELO e SN da ONU:': '',
        'POSSUI COMPUTADOR/NOTEBOOK:': '',
        'QUANTOS DISPOSITIVOS NA RESIDÊNCIA:': '',
        'RELATO:': ''
    },
    'Cobrança de OS': {
        'COBRANÇA DE O.S.': '',
        'TIPO DA O.S.:': '',
        'DENTRO DO PRAZO:': '',
        'SOLICITADA ANTECIPAÇÃO ou COBRADA O.S.?': '' ,
        'TELs de CONTATO:': ''
    },
    'Troca de senha': {
        'TROCA DE SENHA': '',
        'REDE ANTIGA:': '',
        'SENHA ANTIGA:': '',
        'REDE NOVA:': '',
        'SENHA NOVA:': '',
        'DNS PADRÃO: ': '',
        'CLIENTE CONSEGUIU CONECTAR A WIFI?': '',
        'TELs de CONTATO:': ''
    },
    'Liberação de porta': {
        'LIBERAÇÃO DE PORTAS': '',
        'MOTIVO:': '',
        'ACESSO REMOTO VIA IP?': '',
        'POSSUI PC?': '',
        'TELs de CONTATO:': ''
    },
    'Upgrade': {
        'UPGRADE': '',
        'MODELO e SN da ONU:': '',
        'BARRAMENTO: (/100 ou /1000)': ''
    },
    'Teste de velocidade': {
        'TESTE DE VELOCIDADE': '',
        'DOWN e UPLOAD:': '',
        'via CABO ou WIFI:': '',
        'SINAL:': '',
        'MODELO e SN da ONU:': '',
        'RELATO:': ''
    },
}


dicio_os = {
    'Sem conexão': {
'SEM AUTENTICAÇÃO': '',
'SINAL:': '',
'MODELO e SN da ONU:': '',
'TOPOLOGIA:': ''
    },
    'Atenuação': {
'ATENUAÇÃO(LUZ -26 OU MENOR(EX -28 -29 -30 -32):': '',
'SINAL:': '',
'TOPOLOGIA:': ''
    },
    'Oscilação': {
'OSCILAÇÃO:': '',
'SINAL:': '',
'MODELO e SN da ONU:': '',
'ROTEADOR():': '',
'TOPOLOGIA:': '',
'RELATO:': '',
'CLIENTE TEM DISPONIBILIDADE DE ACESSO REMOTO?': ''
    }
}


dicio_n2 = {
    'Oscilação': 
{'OSCILAÇÃO': '',
'PROBLEMA:': '',
'AUTENTICADO: ': '',
'SINAL:': '',
'MODELO e SN da ONU:': '',
'POSSUI COMPUTADOR/NOTEBOOK:': '',
'RELATO: ': '',
'Tel de contato:': ''} ,
    'Sem autenticação': 
{'SEM AUTENTICAÇÃO': '',
'REQUISITANDO PPPOE:': '',
'WAN CONFIGURADA: ': '',
'CONCENTRADOR e VLAN:': '',
'MODELO e SN da ONU:': '',
'Tel de contato:': ''},
    'Teste de velocidade': 
{'TESTE DE VELOCIDADE': '',
'MODELO e SN da ONU:': '',
'DOWN e UPLOAD:': '',
'SINAL:': '',
'RELATO:': ''},
    'Liberação de porta': 
{'LIBERAÇÃO DE PORTA (Inacessível)': '',
'MODELO e SN da ONU:': '',
'CONCENTRADOR e VLAN:': '',
'IP DO CLIENTE:': '',
'ENDEREÇO ou IP de DESTINO:': '',
'PORTAs SOLICITADAs:': ''},
    'Ping': 
{'PING': '',
'MODELO e SN da ONU:': '',
'CONCENTRADOR e VLAN:': '',
'DNS USADO NO TESTE e RESULTADO:': '',
'ENDEREÇO ou IP de DESTINO:': '',
'LATÊNCIA REGISTRADA:': ''},
    'Site inacessivel': 
{'SITE INACESSÍVEL': '',
'MODELO e SN da ONU:': '',
'VERSÃO da FIRMWARE:': '',
'CONCENTRADOR e VLAN:': '',
'IP DO CLIENTE:': '',
'ENDEREÇO ou IP de DESTINO:': ''},
    'VPN': 
{'VPN': '',
'MODELO e SN da ONU:': '',
'VERSÃO da FIRMWARE:': '',
'CONCENTRADOR e VLAN:': '',
'IP DO CLIENTE:': '',
'ENDEREÇO ou IP da VPN:': '',
'FUNCIONA EM OUTRA REDE?': ''},
    'TV': 
{'TV (sem acesso à internet)': '',
'PROBLEMA:': '',
'MODELO e SN da ONU:': '',
'ENDEREÇO ou IP de DESTINO:': '',
'CONCENTRADOR e VLAN:': '',
'MARCA e MODELO da TV:': '',
'QUAL ERRO APRESENTA:': ''},
}


def seleciona_mascara_os(eventObject):
    dicio_masc = {}
    txt = ''
    txt_mascara_os.delete('1.0', END)
    contrato = input_num_contrato.get()
    for c, v in dicio_os.items():
        if c == eventObject.widget.get():
            for key, value in v.items():
                if key not in dicio_masc:
                    if key == 'SINAL:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Luz']
                    elif key == 'MODELO e SN da ONU:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Modelo ONU/SN']
                    elif key == 'TOPOLOGIA:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Topologia']
                    elif key == 'UPTIME':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Uptime']
                    else:
                        dicio_masc[key] = ''

    for chave, valor in dicio_masc.items():
        txt += f'{chave} {valor}"\n"'.replace('"', '')
    txt_mascara_os.insert(END, txt)
    


def seleciona_mascara_n2(eventObject):
    dicio_masc = {}
    txt = ''
    txt_mascara_n2.delete('1.0', END)
    contrato = input_num_contrato.get()
    for c, v in dicio_n2.items():
        if c == eventObject.widget.get():
            for key, value in v.items():
                if key not in dicio_masc:
                    if key == 'SINAL:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Luz']
                    elif key == 'MODELO e SN da ONU:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Modelo ONU/SN']
                    elif key == 'TOPOLOGIA:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Topologia']
                    elif key == 'UPTIME:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Uptime']
                    else:
                        dicio_masc[key] = ''

    for chave, valor in dicio_masc.items():
        txt += f'{chave} {valor}"\n"'.replace('"', '')
    txt_mascara_n2.insert(END, txt)


def sel_mascara_n1(eventObject):
    dicio_masc = {}
    txt = ''
    txt_area_n1.delete('1.0', END)
    contrato = input_num_contrato.get()
    for c, v in dicio_n1.items():
        if c == eventObject.widget.get():
            for key, value in v.items():
                if key not in dicio_masc:
                    if key == 'SINAL:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Luz']
                    elif key == 'MODELO e SN da ONU:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Modelo ONU/SN']
                    elif key == 'TOPOLOGIA:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Topologia']
                    elif key == 'UPTIME:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['Uptime']
                    elif key == 'REDE ANTIGA:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['ssid']
                    elif key == 'SENHA ANTIGA:':
                        dicio_masc[key] = info_cliente[f'{contrato}']['password']
                    else:
                        dicio_masc[key] = ''

    for chave, valor in dicio_masc.items():
        txt += f'{chave} {valor}"\n"'.replace('"', '')
    txt_area_n1.insert(END, txt)

    lbl_ip_link.configure(text=f'{info_cliente[f"{contrato}"]["ip"]}', cursor='hand2', foreground='blue')
    lbl_ip_link.bind('<Button-1>', lambda x: webbrowser.open_new(f'{info_cliente[f"{contrato}"]["ip"]}'))



def seleciona_mascara_sac(eventObject):
    txt = ' '
    txt_area_sac.delete('1.0', END)
    for c, v in dicio_sac.items():
        if c == eventObject.widget.get():
            for key in v.keys():
                txt = txt + key + '\n'

    txt_area_sac.insert(END, txt)



def copiar_mascara():
    if notebook_nivel1_sac.index('current') == 0:
        conteudo = txt_area_n1.get('1.0', END)
        btn_copiar_mascara_n1.clipboard_clear()
        btn_copiar_mascara_n1.clipboard_append(conteudo)
    elif notebook_nivel1_sac.index('current') == 1:
        conteudo = txt_area_sac.get('1.0', END)
        btn_copiar_mascara_n1.clipboard_clear()
        btn_copiar_mascara_n1.clipboard_append(conteudo)


def copiar_solucao():
    if notebook_os_nivel2.index('current') == 0:
        conteudo = txt_mascara_os.get('1.0', END)
        btn_copiar_mascara_n1.clipboard_clear()
        btn_copiar_mascara_n1.clipboard_append(conteudo)
    elif notebook_os_nivel2.index('current') == 1:
        conteudo = txt_mascara_n2.get('1.0', END)
        btn_copiar_mascara_n1.clipboard_clear()
        btn_copiar_mascara_n1.clipboard_append(conteudo)


def limpar_tudo():
    txt_area_n1.delete('1.0', END)
    txt_area_sac.delete('1.0', END)
    txt_mascara_os.delete('1.0', END)
    txt_mascara_n2.delete('1.0', END)
    input_num_contrato.delete(0, END)
    lbl_ip_link.configure(text='')


def janela_abrir_os():
    janela_OS = Toplevel()
    janela_OS.geometry("500x250")
    janela_OS.title('Abrir OS')

    janela_OS.focus_set()
    janela_OS.grab_set()

    lbl_tipo_os = Label(janela_OS, text='Escolha o tipo da OS')

    tipos_os = (
        'Sem conexão',
        'Oscilação',
        'Atenuação',
        'Retorno de OS',
        'Mudança de endereço',
        'Mudança interna',
        'Upgrade'
    )
    cbx_abrir_os = Combobox(janela_OS, values=tipos_os)

    lbl_tipo_os.place(x=10, y=20)
    cbx_abrir_os.place(x=10, y=40)

    janela_OS.mainloop()



janela = Tk()
janela.geometry('900x680')
janela.resizable(False, False)
janela.title('Wantel Unify')


# Labels
lbl_num_contrato = Label(janela, text='Número do contrato')
lbl_ip = Label(janela, text='IP: ')
lbl_ip_link = Label(janela, text='')
lbl_teve_os = Label(janela, text='Teve OS: Sim, oscilação com menos de 30 dias.')

lbl_teve_os.place(x=320, y=40)
lbl_ip.place(x=150, y=40)
lbl_ip_link.place(x=170, y=40)
lbl_num_contrato.place(x=10, y=10)

# Inputs
input_num_contrato = Entry(janela, width=17)
input_num_contrato.place(x=10, y=40)

# Botões
btn_buscar = Button(janela, width=15, text='Buscar')
btn_reiniciar_onu = Button(janela, width=15, text='Reiniciar ONU')
btn_abrir_os = Button(janela, width=15, text='Abrir OS', command=janela_abrir_os)
btn_verificar_infra = Button(janela, width=15, text='Verificar Infra')
btn_limpar = Button(janela, width=15, text='Limpar Tudo', command=limpar_tudo)

btn_buscar.place(x=10, y=70)
btn_reiniciar_onu.place(x=150, y=70)
btn_abrir_os.place(x=290, y=70)
btn_verificar_infra.place(x=430, y=70)
btn_limpar.place(x=570, y=70)

# Notebook principal
notebook_principal = Notebook(janela)
notebook_principal.place(x=0, y=120)

# Frames = Tabs
tab_visao_geral = Frame(notebook_principal, width=900, height=600)
tab_st = Frame(notebook_principal, width=900, height=600)

tab_visao_geral.place(x=10, y=10)

# Adicionando as Tabs no notebook principal
notebook_principal.add(tab_visao_geral, text='Informações Gerais')
notebook_principal.add(tab_st, text='Suporte Técnico/SAC')

# Text area visão geral
txt_visao_geral = Text(tab_visao_geral, width=900, height=680)
txt_visao_geral.place(x=0, y=0)

# Elementos da aba Suporte Técnico
lbl_tipo_mascara = Label(tab_st, text='Máscara nível 1')
lbl_mascara_sac = Label(tab_st, text='Máscara SAC').place(x=255, y=10)
mascara_n1 = (
    'Sem conexão', 
    'Lentidão/Oscilação', 
    'Cobrança de OS', 
    'Liberação de porta', 
    'Troca de senha', 
    'Teste de velocidade', 
    'Upgrade')
cbx_mascaras_n1 = Combobox(tab_st, values=mascara_n1)
cbx_mascaras_n1.bind('<<ComboboxSelected>>', sel_mascara_n1)

mascara_sac = (
    'Boleto',
    'Desbloqueio',
    'Duvida',
    'Comprovante de pagamento',
    'Upgrade/Downgrade',
    'Suspensão de contrato/Ativação',
    'SVA',
    'Indicação de amigo',
    'Troca de titularidade',
    'Mudança de endereço',
    'Mudança de local',
    'Alteração de vencimento',
    'Inversão de pagamento',
    'Estorno',
    'Nota fiscal',
    'Negociação',
    'Duplicidade de pagamento',
)

cbx_mascara_sac = Combobox(tab_st, values=mascara_sac)
cbx_mascara_sac.bind('<<ComboboxSelected>>', seleciona_mascara_sac)

btn_copiar_mascara_n1 = Button(tab_st, text='Copiar', width=15, command=copiar_mascara)

notebook_nivel1_sac = Notebook(tab_st)
notebook_nivel1_sac.place(x=10, y=120)

tab_mascara_n1 = Frame(notebook_nivel1_sac, width=400, height=370)
tab_mascara_sac = Frame(notebook_nivel1_sac, width=400, height=370)

notebook_nivel1_sac.add(tab_mascara_n1, text='Máscara nível 1')
notebook_nivel1_sac.add(tab_mascara_sac, text='Máscara SAC')

txt_area_n1 = Text(tab_mascara_n1, width=400, height=370)
txt_area_sac = Text(tab_mascara_sac, width=400, height=370)
txt_area_sac.config(wrap='word')

txt_area_n1.place(x=0, y=0)
txt_area_sac.pack()
txt_area_sac.place(bordermode=OUTSIDE, height=370, width=400)
lbl_tipo_mascara.place(x=10, y=10)
cbx_mascaras_n1.place(x=10, y=40)
cbx_mascara_sac.place(x=255, y=40)
btn_copiar_mascara_n1.place(x=10, y=80)


# Notebook OS e Nivel 2
notebook_os_nivel2 = Notebook(tab_st)
notebook_os_nivel2.place(x=480, y=120)

tab_mascara_os = Frame(notebook_os_nivel2, width=400, height=370)
tab_mascara_n2 = Frame(notebook_os_nivel2, width=400, height=370)

notebook_os_nivel2.add(tab_mascara_os, text='Máscara OS')
notebook_os_nivel2.add(tab_mascara_n2, text='Máscara nível 2')

txt_mascara_os = Text(tab_mascara_os, width=400, height=370)
txt_mascara_os.place(x=0, y=0)
txt_mascara_n2 = Text(tab_mascara_n2, width=400, height=370)
txt_mascara_n2.place(x=0, y=0)

lbl_mascara_os = Label(tab_st, text='Máscara OS').place(x=480, y=10)
lbl_mascara_nivel2 = Label(tab_st, text='Máscara nível 2').place(x=725, y=10)


mascara_os = (
    'Sem conexão',
    'Atenuação',
    'Oscilação',
)
cbx_mascara_os = Combobox(tab_st, values=mascara_os)
cbx_mascara_os.bind('<<ComboboxSelected>>', seleciona_mascara_os)
mascara_nivel2 = (
    'Oscilação',
    'Sem autenticação',
    'Teste de velocidade',
    'Liberação de porta',
    'Ping',
    'Site inacessivel',
    'VPN',
    'TV'
)
cbx_mascara_nivel2 = Combobox(tab_st, values=mascara_nivel2)
cbx_mascara_nivel2.bind('<<ComboboxSelected>>', seleciona_mascara_n2)
btn_copiar_solucao = Button(tab_st, text='Copiar', width=15, command=copiar_solucao)

cbx_mascara_os.place(x=480, y=40)
cbx_mascara_nivel2.place(x=725, y=40)
btn_copiar_solucao.place(x=480, y=80)




janela.mainloop()