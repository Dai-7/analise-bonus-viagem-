import pandas as pd

from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACce4d0a2274913519efd23a202d7a938b"
# Your Auth Token from twilio.com/console
auth_token  = "b0b3b07241fb496bb60feb9eca99f2dc"

client = Client(account_sid, auth_token)

#pandas openpyxl(integração python excel) twilio(sms)
#passo a passo de solução
# abrir os 6 arquivos em excel
lista_meses=['janeiro(1)','fevereiro','março','abril','maio','junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000) .any():
        vendedor=tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas=tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta.Vendedor:{vendedor}, Vendas:{vendas}')
        message = client.messages.create(
        to="+5551992287176",
        from_="+16505031711",
        body=f'No mês {mes} alguem bateu a meta.Vendedor:{vendedor}, Vendas:{vendas}')
        print(message.sid)
#para cada arquivo verificar se algum valor na coluna vendas naquele arquivo é maior que 55 mil
# se for maoir que 55 mil envia um sms
# se for maior do que 55 mil -> envia um sms com o nome o mes e as vendas do vendedor
# caso não seja maior que 55 mil nao fazer nada

