# Funçao para carregar tarefas do arquivo
def carregar_tarefas():
    tarefas = []
    try:
        with open('tarefas.txt', 'r') as arquivo:
            for linha in arquivo:
                tarefa = linha.strip().split('|')
                tarefas.append({'id': int(tarefa[0]), 'nome': tarefa[1], 'status': tarefa[2]} )
    except FileNotFoundError:
        pass # se o arquivo não existir ainda, retorna uma lista vazia.
    return tarefas
# Função para salvar as tarefas no arquivo
def salvar_tarefas(tarefas):
    with open('tarefas.txt', 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa['id']}|{tarefa['nome']}|{tarefa['status']}\n")
# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    nome_tarefa = input("Digite o nome da tarefa:")
    id_tarefa = len(tarefas) + 1 # Gera um id único para a tarefa
    tarefa = {'id':id_tarefa, 'nome':nome_tarefa, 'status': 'pendente'}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")
# Função para listar todas as tarefas
def listar_tarefas(tarefas):
    if tarefas:
        print("Lista de tarefas:")
        for tarefa in tarefas:
            print(f"{tarefa['id']}, {tarefa['nome']}, {tarefa['status']}")
    else:
        print("Nenhuma tarefa cadastrada!")
# Função para editar uma tarefa
def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    id_tarefa = int(input("Digite o ID da tarefa que deseja editar: "))
    tarefa = next((t for t in tarefas if t['id'] == id_tarefa), None)
    if tarefa:
        novo_nome = input(f"Digite o novo nome para a tarefa, {tarefa['nome']}': ")
        tarefa['nome'] = novo_nome
        salvar_tarefas(tarefas)
        print("Tarefa editada com sucesso!")
    else:
        print("Tarefa não encontrada")
# Função para remover uma tarefa
def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))
        print("Verificando lista de tarefas:")
        for tarefa in tarefas:
            print(f"ID:{tarefa['id']}, Nome:{tarefa['nome']}, Status:{tarefa['status']}")
            tarefa_para_remover = tarefa
            break
        if tarefa_para_remover:
            tarefas.remove(tarefa_para_remover)
            print("Tarefa removida com sucesso!")
            for i, tarefa in enumerate(tarefas):
                tarefa['id'] = i + 1
                salvar_tarefas(tarefas)
        else:
            print("Tarefa com ID fornecido não foi encontrado.")
    except ValueError:
        print("Por favor, insira um numero válido para o ID.")
# Função principal que gerencia o menu
def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\nGerenciador de Tarefas:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Editar Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            editar_tarefa(tarefas)
        elif escolha == '4':
            remover_tarefa(tarefas)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção invalida!")
# chamada da função principal
menu()

