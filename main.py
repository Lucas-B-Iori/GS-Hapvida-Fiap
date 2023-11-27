# A função valida_respostas verifica se um input digitado pelo usuario esta dentre as possíveis opçoes válidas
def valida_resposta(msg, lista):
    resposta = input(msg).lower()
    while resposta not in lista:
        print("Resposta inválida")
        resposta = input(msg)
    return resposta


# A função transforma_em_numero verifica se o input do usuário é um numero e se for retorna ele no formato de numero
def transforma_em_numero(msg):
    dado = input(msg)
    while not dado.isnumeric():
        print("Essa informação precisa ser um numero inteiro")
        dado = input(msg)
    return int(dado)


# A função calcula_imc recebe a altura e o peso do usuário e retorna o imc calculado e arredondado com 2 casas decimais
def calcula_imc(altura, peso):
    h = altura / 100
    imc = peso / (h * h)
    return round(imc, 2)


# A função verifica_cadastro_usuario recebe uma lista e o nome do usuário,
# pode ser usada tanto pra medicos quanto pra paciente
def verifica_cadastro_usuario(lista, nome_usuario):
    for el in lista:
        if el[0].lower() == nome_usuario.lower():
            return True
    return False


# A função cria_paciente recebe uma lista, pede todas as informações do paciente e
# coloca esse novo paciente no final da lista
def cria_paciente(lista):
    nome = input("Digite o nome completo do paciente: ")
    altura = transforma_em_numero("Escreva qual a altura do paciente em centímetros: ")
    peso = transforma_em_numero("Digite o peso aproximado do paciente: ")
    sexo = valida_resposta("Digite qual o sexo do paciente: ", ['feminino', 'masculino'])
    imc = calcula_imc(altura, peso)
    consulta = 'Nenhuma'
    paciente = [nome, altura, peso, sexo, imc, consulta]
    lista.append(paciente)


# A função cria_medico, recebe uma lista, pede o nome e especialização do médico
# e coloca esse novo médico dentro da lista
def cria_medico(lista):
    nome = input("Digite o nome completo do medico: ")
    especialidade = input("Digite a sua especialização: ")
    medico = [nome, especialidade]
    lista.append(medico)


# A função valida_usuario_escolhido recebe uma lista e uma mensagem, seleciona com uma lista chamada nomes
# apenas os nomes dos pacientes/médicos e verifica se o usuário escolhido é valido
def valida_usuario_escolhido(lista, msg):
    nomes = []
    for i in range(len(lista)):
        nomes.append((lista[i][0].lower()))
    usuario_escolhido = valida_resposta(f"{msg}, \n{nomes}", nomes)
    return usuario_escolhido


# A função mostra_infos_pacientes recebe uma lista e o paciente que foi escolhido, ela percorre a lista
# até achar o paciente escolhido e printa todas as suas informações
def mostra_infos_paciente(lista, paciente_escolhido):
    for paciente in lista:
        if paciente[0].lower() == paciente_escolhido.lower():
            print(f"Nome Completo: {paciente[0]}")
            print(f"Altura(cm): {paciente[1]}")
            print(f"Peso(kg): {paciente[2]}")
            print(f"Sexo: {paciente[3]}")
            print(f"IMC: {paciente[4]}")
            print(f"Consulta: {paciente[5]}")
            print()
            break


# A função altera_dados_paciente recebe uma lista, o dado selecionado e o paciente escolhido,
# primeiramente ela define melhor qual tipo de dado é esse, depois acha o paciente escolhido na lista
# e altera o dado em questão
def altera_dados_paciente(lista, dado_escolhido, paciente_escolhido):
    if dado_escolhido == 1:
        dado = "nome completo"
    elif dado_escolhido == 2:
        dado = "altura"
    elif dado_escolhido == 3:
        dado = "peso"
    else:
        dado = "sexo"
    for paciente in lista:
        if paciente[0].lower() == paciente_escolhido.lower():
            print(
                f"{dado.capitalize()} do(a) paciente {paciente_escolhido.capitalize()}: {paciente[dado_escolhido - 1]}")
            paciente[dado_escolhido - 1] = input("Digite um novo valor para esse dado: ")
            break


# A função valida_data não recebe nenhum parâmetro, apenas faz verificações para saber se o dia e mes
# são validos ou não, e por fim retorna uma fstring com dia, mes e ano
def valida_data():
    dia = transforma_em_numero("Digite qual vai ser o dia da consulta: ")
    while dia > 31:
        dia = transforma_em_numero("Digite qual vai ser o dia da consulta: ")
    mes = transforma_em_numero("Digite qual vai ser o mes da consulta: ")
    while mes > 12:
        mes = transforma_em_numero("Digite qual vai ser o mes da consulta: ")
    ano = 2023
    if mes < 12:
        ano = 2024
    return f"{dia}/{mes}/{ano}"


# A função marca_consulta recebe o paciente e a lista, pergunta pro usuario com qual médico e em qual dia
# a consulta será marcada, essas duas informações são validadas através de outras funções, por fim
# percorre a lista passada para mudar a informação sobre consulta no paciente determinado
def marca_consulta(paciente, lista):
    print("Médicos da casa: ")
    for medico in lista_medicos:
        print(f'{medico[0]} - {medico[1]}')
    medico_escolhido = valida_usuario_escolhido(lista_medicos, 'Qual médico você vai querer marcar uma consulta? ')
    data = valida_data()
    for el in lista:
        if el[0].lower() == paciente.lower():
            el[5] = f"{medico_escolhido} - {data}"
            print(f"Consulta Marcada: {el[5]}")
            break


# Primeiro, é feita uma verificação para saber se quem esta usando o programa é um médico ou um paciente
opcoes_usuario = ['medico', 'paciente']
usuario = valida_resposta("Qual a sua função? medico ou paciente? ", opcoes_usuario)

# Lista de Pacientes guarda todas as informações sobre eles, na ordem: Nome Completo,
# altura(cm), peso(kg), sexo, IMC, consulta
lista_pacientes = [
    ['Ana Silva', 165, 60, 'feminino', 22.04, 'Nenhuma'],
    ['Felipe Oliveira', 178, 75, 'masculino', 23.67, 'Nenhuma'],
    ['Marina Santos', 170, 68, 'feminino', 23.53, 'Nenhuma'],
    ['Rafael Lima', 175, 80, 'masculino', 26.12, 'Nenhuma'],
    ['Carolina Costa', 160, 55, 'feminino', 21.48, 'Nenhuma']
]

# Lista de Medicos guarda o nome completo e a especialização de cada um
lista_medicos = [
    ['Carolina Pereira', 'Cardiologia'],
    ['Ricardo Almeida', 'Ortopedia'],
    ['Camila Costa', 'Ginecologia e Obstetrícia'],
    ['Gustavo Santos', 'Pediatria'],
    ['Mariana Oliveira', 'Neurologia']
]

if usuario == 'medico':
    nome_medico = input("Digite o seu nome completo: ")
    # Verifica se o medico ja esta cadastrado
    if not verifica_cadastro_usuario(lista_medicos, nome_medico):
        print("Hm, você ainda não está cadastrado(a) no nosso sistema, vamos resolver isso!")
        cria_medico(lista_medicos)

    # Uma vez que o medico ja esta cadastrado, o menu de opção é mostrado para que ele acesse e escolha uma opção
    print("Você ja esta cadastrado no sistema!")
    while True:
        opcoes_validas_medico = ["1", "2", "3", "4"]
        opcao_escolhida = valida_resposta("\nSelecione opção desejada: "
                                          "\nDigite 1 para cadastrar novo paciente"
                                          "\nDigite 2 para ver informações de algum paciente"
                                          "\nDigite 3 para mudar informações de um paciente"
                                          "\nDigite 4 para sair\n", opcoes_validas_medico)
        # Opção 1 é utilizada para cadastrar um novo paciente no sistema
        if opcao_escolhida == '1':
            cria_paciente(lista_pacientes)
        # Opção 2 é utilizada para mostrar as informações de um paciente
        elif opcao_escolhida == '2':
            paciente_escolhido = valida_usuario_escolhido(lista_pacientes, "Qual paciente você vai querer ver as "
                                                                           "informações?")
            mostra_infos_paciente(lista_pacientes, paciente_escolhido)
        # Opção 3 é utilizada para alterar alguma informação de um paciente específico
        elif opcao_escolhida == '3':
            paciente_escolhido = valida_usuario_escolhido(lista_pacientes, 'Qual paciente você vai querer ver as '
                                                                           'informações?')
            while True:
                dados_valido_para_escolha = ['1', '2', '3', '4', '5']
                dado_escolhido = valida_resposta(f"\nSelecione o dado do(a) paciente {paciente_escolhido.capitalize()}"
                                                 f" que deseja alterar:"
                                                 "\nDigite 1 para nome completo"
                                                 "\nDigite 2 para altura"
                                                 "\nDigite 3 para peso"
                                                 "\nDigite 4 para sexo"
                                                 "\nDigite 5 para sair\n", dados_valido_para_escolha)
                dado_escolhido = int(dado_escolhido)
                if dado_escolhido == 5:
                    break
                altera_dados_paciente(lista_pacientes, dado_escolhido, paciente_escolhido)
        # Opcão 4 é usada para sair do programa
        else:
            break
else:
    nome_paciente = input("Digite o seu nome: ")
    # Verifica se o paciente ja esta cadastrado
    if not verifica_cadastro_usuario(lista_pacientes, nome_paciente):
        print("Hm, você ainda não está cadastrado(a) no nosso sistema, vamos resolver isso!")
        cria_paciente(lista_pacientes)
        nome_paciente = lista_pacientes[len(lista_pacientes) - 1][0]

    print("Você ja esta cadastrado no sistema!")
    # Uma vez que o paciente ja esta cadastrado, o menu de opção é mostrado para que ele acesse e escolha uma opção
    while True:
        opcoes_validas_paciente = ["1", "2", "3"]
        opcao_desejada = valida_resposta("\nSelecione a opção desejada: \n"
                                         "Digite 1 para consultar seus dados\n"
                                         "Digite 2 para marcar uma consulta com algum médico\n"
                                         "Digite 3 para sair\n", opcoes_validas_paciente)
        # Opção 1 é usada para mostrar informações sobre o paciente
        if opcao_desejada == '1':
            mostra_infos_paciente(lista_pacientes, nome_paciente)
        # opção 2 é usada para marcar uma consulta com algum médico
        elif opcao_desejada == '2':
            marca_consulta(nome_paciente, lista_pacientes)
        else:
            break
