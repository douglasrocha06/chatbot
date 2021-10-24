import telebot

CHAVE_API = "2083867788:AAEXfM8dh7C8ffEB5Zc12n8Kf-RjWgkIqCI"

bot = telebot.TeleBot(CHAVE_API)

#Investimentos
@bot.message_handler(commands=["I"])
def opcao1(mensagem):
    texto = """
    Abaixo temos as principais dúvidas relacionadas a investimentos, fique a vontade e esperamos poder sanar todas elas!!\n
/01 - O que é bolsa de valores?
/02 - O que é renda fixa?
/03 - O que é renda variável?
/04 - O que significa pregão?
/05 - Qual é a representatividade do touro na bolsa de valores?
/06 - O que o urso significa para a bolsa de valores?
/07 - Qual o significa de Bull Market e Bear Market?
/08 - O que é Circuit Breaking?
/09 - O que é análise técnica?
/010 - O que significa análise fundamentalista?"""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["01"])
def I(mensagem):
    bot.send_message(mensagem.chat.id, "A bolsa de valores é um ambiente de negociação no qual investidores podem comprar ou vender seus títulos emitidos por empresas, sejam elas com capitais públicos, mistos ou privados. Esse processo é intermediado com auxílio de correspondentes de negociações através de corretoras.\n\nPara ter uma ideia mais clara do que é a bolsa, é possível fazer uma analogia. Imagine uma feira, onde produtores expõem seus produtos para a clientela comprar. A bolsa de valores opera de forma semelhante: se você decide vender uma ação e outro investidor tem interesse em comprá-la, ela será o ponto de encontro entre vocês.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["02"])
def II(mensagem):
    bot.send_message(mensagem.chat.id, "Renda fixa é uma título atrelado a uma taxa, como por exemplo a Selic, títulos do tesouro direto entre outros.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["03"])
def III(mensagem):
    bot.send_message(mensagem.chat.id, "Renda variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["04"])
def IV(mensagem):
    bot.send_message(mensagem.chat.id, "Renda variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["05"])
def V(mensagem):
    bot.send_message(mensagem.chat.id, "Renda variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["06"])
def VI(mensagem):
    bot.send_message(mensagem.chat.id, "Renda variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["07"])
def VII(mensagem):
    bot.send_message(mensagem.chat.id, "Renda variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["08"])
def VIII(mensagem):
    bot.send_message(mensagem.chat.id, "Renda variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["09"])
def IX(mensagem):
    bot.send_message(mensagem.chat.id, "Renda variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["010"])
def X(mensagem):
    bot.send_message(mensagem.chat.id, "variável significa investimento que possuem volatidade, como por exemplo a bolsa de valores.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

#Imposto
@bot.message_handler(commands=["II"])
def opcao2(mensagem):
    texto = """
    Abaixo temos as principais dúvidas relacionadas a impostos na bolsa de valores, fique a vontade e esperamos poder saná-lás!!\n
/1 - O que acontece se não declarar ações?
/2 - Como declarar venda de ações abaixo de 20 mil?
/3 - Como pagar Darf de day trade atrasado?
/4 - O que acontece se eu não pagar a DARF de operações em Day trade?
/5 - Realizei venda de fundos imobiliário com lucro devo pagar darf?
/6 - Quando devo pagar DARF de Fundo de Investimentos Imobiliário?
/7 - Como calcular imposto de renda na venda de fundos de investimento imobiliário?
/8 - Qual o valor mínimo para pagar o DARF?
/9 - Quem declara o Imposto de Renda atrasado quando é restituído pela Receita Federal?
/10 - Perdi dinheiro na bolsa de valores, mesmo assim preciso declarar imposto de renda?"""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["1"])
def I(mensagem):
    bot.send_message(mensagem.chat.id, "A omissão de informações sobre investimentos em renda variável pode levar o contribuinte para a malha fina da Receita Federal. A multa pode chegar a 150% do valor do imposto devido sobre o ganho com as ações. A Receita tem até cinco anos para cobrar o imposto com multa.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["2"])
def II(mensagem):
    bot.send_message(mensagem.chat.id, "Vendas de ações no valor de até 20.000 reais em um mesmo mês não são tributadas. Nesse caso, você deve subtrair o custo de aquisição do valor obtido com a venda e informar esse lucro na ficha de “Rendimentos isentos e não tributáveis”, na linha 18 — “Ganhos líquidos em operações no mercado à vista de ações.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["3"])
def III(mensagem):
    bot.send_message(mensagem.chat.id, "Se você esqueceu de pagar o DARF em um mês, é possível emiti-lo novamente realizando via web. Ao preencher os dados, ele já calcula a multa, que, por sua vez, é de 0,33% ao dia, com um teto de 20% sobre o valor devido como pagamento do Imposto\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["4"])
def IV(mensagem):
    bot.send_message(mensagem.chat.id, "O investidor que não paga o DARF mensal sobre day trade sofre multa e juros de 0,33% ao dia sobre o valor devido. O limite é de 20% do total e também será corrigido pela taxa Selic enquanto seguir sem pagar\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["5"])
def V(mensagem):
    bot.send_message(mensagem.chat.id, "As operações realizadas em FIIs também não possuem isenção. Logo, se você vender um ativo com lucro terá que gerar o seu DARF. Nesse caso, a alíquota é de 20% sobre os resultados do período independentemente do tipo de operação (day trade ou posição)\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["6"])
def VI(mensagem):
    bot.send_message(mensagem.chat.id, "Em fundos imobiliários, há incidência de Imposto de Renda na venda de cotas quando a operação gera lucros ao investidor. Sempre que esse tipo de transação ocorre, o investidor deve emitir o DARF e quitá-lo até o último dia útil do mês seguinte ao da apuração.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["7"])
def VII(mensagem):
    bot.send_message(mensagem.chat.id, "Para fazer o cálculo do imposto de renda, você deve utilizar o preço médio de aquisição por cota. No caso do exemplo acima, o valor é R$8,80. Caso você venda 50 cotas, o seu custo de aquisição terá sido de R$440 (8,80 x 50). As 200 cotas restantes terão custo de R$1.760 (200 x 8,80)\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["8"])
def VIII(mensagem):
    bot.send_message(mensagem.chat.id, "O imposto ou contribuição administrado pela Secretaria da Receita Federal, arrecadado sob um determinado código de receita, que, no período de apuração, resultar inferior a R$ 10,00 (dez reais), deverá ser adicionado ao imposto ou contribuição de mesmo código, correspondente aos períodos subsequentes.\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["9"])
def IX(mensagem):
    bot.send_message(mensagem.chat.id, "A Receita dá um prazo de cinco anos para receber o documento atrasado. Depois de enviar, o cidadão pode inclusive ter restituição a receber. Mas vale lembrar que será cobrada multa de 1% ao mês sobre o valor do imposto atrasado\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

@bot.message_handler(commands=["10"])
def X(mensagem):
    bot.send_message(mensagem.chat.id, "Havendo ganho ou perda nas operações day trade (compra e venda em um único dia) o contribuinte é obrigado entregar a declaração e isso vale também para quem operou e entra na declaração de outra pessoa como de dependente, como é o seu caso. Não existe isenção de IR nessas operações\n\nSelecione uma opção abaixo para: \n/voltar\n/inicio")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá seja bem vindo ao IR INFORM!\n\nEste é uma canal especializado em tirar as principais dúvidas dos nossos clientes sobre investimentos e impostos da bolsa de valores.\n
Nos informe em qual assunto está relacionada a sua dúvida.
/I - Investimentos
/II - Impostos
     
Clique em uma das opções acima."""
    bot.reply_to(mensagem, texto)

bot.polling()