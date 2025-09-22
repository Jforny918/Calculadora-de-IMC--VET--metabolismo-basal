import json
import os
import math

# Arquivo para salvar pacientes
ARQUIVO_PACIENTES = 'pacientes.json'

def carregar_pacientes():
    """Carrega pacientes de um arquivo JSON."""
    if os.path.exists(ARQUIVO_PACIENTES):
        with open(ARQUIVO_PACIENTES, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_pacientes(pacientes):
    """Salva pacientes em um arquivo JSON."""
    with open(ARQUIVO_PACIENTES, 'w', encoding='utf-8') as f:
        json.dump(pacientes, f, indent=4, ensure_ascii=False)

def calcular_imc(peso, altura):
    """Calcula IMC e retorna categoria."""
    imc = peso / (altura / 100) ** 2
    if imc < 18.5:
        categoria = "Baixo peso"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    return imc, categoria

def calcular_mb(peso, altura, idade, sexo):
    """Calcula Metabolismo Basal (Harris-Benedict revisada)."""
    if sexo.upper() == 'M':
        return 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    else:
        return 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

def calcular_vet(mb, nivel_atividade):
    """Calcula VET baseado no nível de atividade."""
    fatores = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    return mb * fatores.get(nivel_atividade, 1.2)

def calcular_macros(vet, peso, objetivo):
    """Calcula macros baseados no objetivo."""
    prot_g = peso * 2.0  # Média 2g/kg para prot
    prot_kcal = prot_g * 4
    
    if objetivo == 1:  # Hipertrofia: superávit 15%
        vet_alvo = vet * 1.15
        carb_g = peso * 5.0  # 5g/kg
        carb_kcal = carb_g * 4
        gord_kcal = vet_alvo - prot_kcal - carb_kcal
        gord_g = gord_kcal / 9 if gord_kcal > 0 else 0
    elif objetivo == 2:  # Emagrecimento: déficit 20%
        vet_alvo = vet * 0.8
        carb_kcal = 0.50 * vet_alvo
        gord_kcal = 0.25 * vet_alvo
        carb_g = carb_kcal / 4
        gord_g = gord_kcal / 9
    else:  # Manutenção
        vet_alvo = vet
        carb_kcal = 0.50 * vet_alvo
        gord_kcal = 0.25 * vet_alvo
        carb_g = carb_kcal / 4
        gord_g = gord_kcal / 9
    
    return {
        'vet_alvo': vet_alvo,
        'prot_g': round(prot_g, 1), 'prot_kcal': round(prot_kcal, 1),
        'carb_g': round(carb_g, 1), 'carb_kcal': round(carb_kcal, 1),
        'gord_g': round(gord_g, 1), 'gord_kcal': round(gord_kcal, 1)
    }

def sugestoes_alimentos(macro, tipo_refeicao):
    """Sugestões genéricas de alimentos por macro e refeição."""
    sugestoes = {
        'prot': {'café': 'Ovos, iogurte grego', 'lanche': 'Queijo cottage, shake de whey', 'almoço': 'Frango grelhado, peixe', 'janta': 'Carne magra, tofu'},
        'carb': {'café': 'Aveia, pão integral', 'lanche': 'Fruta com granola', 'almoço': 'Arroz integral, batata doce', 'janta': 'Quinoa, massas integrais'},
        'gord': {'café': 'Abacate, nozes', 'lanche': 'Azeite em salada', 'almoço': 'Azeite, sementes', 'janta': 'Salmão, azeitonas'}
    }
    return sugestoes.get(macro, {}).get(tipo_refeicao, 'Alimentos variados')

def dividir_refeicoes(macros):
    """Divide macros em 6 refeições (aprox: 20% café, 15% l1, 25% almoço, 15% l2, 25% janta, 10% ceia)."""
    percentuais = [0.20, 0.15, 0.25, 0.15, 0.25, 0.10]
    refeicoes = ['Café da Manhã', 'Lanche da Manhã', 'Almoço', 'Lanche da Tarde', 'Janta', 'Ceia']
    divisao = []
    for i, perc in enumerate(percentuais):
        prot_g = macros['prot_g'] * perc
        carb_g = macros['carb_g'] * perc
        gord_g = macros['gord_g'] * perc
        divisao.append({
            'refeicao': refeicoes[i],
            'prot_g': round(prot_g, 1),
            'carb_g': round(carb_g, 1),
            'gord_g': round(gord_g, 1),
            'sugestao': f"Prot: {sugestoes_alimentos('prot', refeicoes[i].lower())}; Carb: {sugestoes_alimentos('carb', refeicoes[i].lower())}; Gord: {sugestoes_alimentos('gord', refeicoes[i].lower())}"
        })
    return divisao

def menu_principal():
    pacientes = carregar_pacientes()
    while True:
        print("\n" + "="*50)
        print("PROGRAMA DE CÁLCULO NUTRICIONAL PARA NUTRICIONISTAS")
        print("="*50)
        print("1. Cadastrar Novo Paciente")
        print("2. Carregar Paciente Existente")
        print("3. Listar Todos os Pacientes")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            nome = input("Nome do paciente: ").strip()
            if nome in pacientes:
                print("Paciente já existe! Carregando dados existentes.")
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (cm): "))
            idade = int(input("Idade (anos): "))
            sexo = input("Sexo (M/F): ").upper()
            if sexo not in ['M', 'F']:
                sexo = 'F'  # Padrão
                print("Sexo inválido. Usando 'F' como padrão.")
            
            # Nível de atividade
            print("\nNível de Atividade:")
            print("1 - Sedentário (pouco ou nenhum exercício)")
            print("2 - Pouco Ativo (exercício leve 1-3 dias/sem)")
            print("3 - Moderadamente Ativo (exercício moderado 3-5 dias/sem)")
            print("4 - Ativo (exercício intenso 5-6 dias/sem)")
            print("5 - Muito Ativo (exercício muito intenso ou trabalho físico)")
            nivel = int(input("Escolha (1-5): "))
            if nivel not in [1,2,3,4,5]:
                nivel = 1
                print("Nível inválido. Usando 1 (sedentário).")
            
            # Objetivo
            print("\nObjetivo:")
            print("1 - Hipertrofia (Ganho de Massa Muscular)")
            print("2 - Emagrecimento (Perda de Gordura)")
            print("3 - Manutenção de Peso")
            objetivo = int(input("Escolha (1-3): "))
            if objetivo not in [1,2,3]:
                objetivo = 3
                print("Objetivo inválido. Usando 3 (manutenção).")
            
            # Cálculos
            imc, categoria_imc = calcular_imc(peso, altura)
            mb = calcular_mb(peso, altura, idade, sexo)
            vet = calcular_vet(mb, nivel)
            macros = calcular_macros(vet, peso, objetivo)
            
            # Salvar paciente
            pacientes[nome] = {
                'peso': peso, 'altura': altura, 'idade': idade, 'sexo': sexo,
                'nivel': nivel, 'objetivo': objetivo,
                'imc': round(imc, 2), 'categoria_imc': categoria_imc,
                'mb': round(mb, 1), 'vet': round(vet, 1),
                'macros': macros
            }
            salvar_pacientes(pacientes)
            print(f"\nPaciente {nome} cadastrado com sucesso!")
            print_resumo(nome, pacientes[nome])
            
            # Opção para gerar plano
            gerar_plano = input("Gerar plano de dieta simples? (s/n): ").lower()
            if gerar_plano == 's':
                gerar_plano_dieta(nome, pacientes[nome])
        
        elif opcao == '2':
            nome = input("Nome do paciente: ").strip()
            if nome in pacientes:
                print_resumo(nome, pacientes[nome])
                # Recalcular se necessário
                recalcular = input("Recalcular macros com novos dados? (s/n): ").lower()
                if recalcular == 's':
                    # Re-digitam dados (simplificado; pode expandir)
                    peso = float(input("Novo peso (kg): "))
                    # ... (adicionar outros se necessário)
                    pacientes[nome]['peso'] = peso
                    # Recalcular tudo
                    imc, categoria_imc = calcular_imc(peso, pacientes[nome]['altura'])
                    mb = calcular_mb(peso, pacientes[nome]['altura'], pacientes[nome]['idade'], pacientes[nome]['sexo'])
                    vet = calcular_vet(mb, pacientes[nome]['nivel'])
                    macros = calcular_macros(vet, peso, pacientes[nome]['objetivo'])
                    pacientes[nome].update({
                        'peso': peso, 'imc': round(imc, 2), 'categoria_imc': categoria_imc,
                        'mb': round(mb, 1), 'vet': round(vet, 1), 'macros': macros
                    })
                    salvar_pacientes(pacientes)
                    print_resumo(nome, pacientes[nome])
                    gerar_plano = input("Gerar novo plano de dieta? (s/n): ").lower()
                    if gerar_plano == 's':
                        gerar_plano_dieta(nome, pacientes[nome])
            else:
                print("Paciente não encontrado!")
        
        elif opcao == '3':
            if not pacientes:
                print("Nenhum paciente cadastrado.")
            else:
                for nome, dados in pacientes.items():
                    print(f"- {nome}: {dados['peso']}kg, IMC {dados['imc']} ({dados['categoria_imc']}), Objetivo {dados['objetivo']}")
        
        elif opcao == '4':
            print("Saindo... Obrigado por usar o programa!")
            break
        
        else:
            print("Opção inválida!")

def print_resumo(nome, dados):
    """Imprime resumo do paciente."""
    macros = dados['macros']
    print(f"\nRESUMO PARA {nome.upper()}")
    print(f"IMC: {dados['imc']} ({dados['categoria_imc']})")
    print(f"Metabolismo Basal: {dados['mb']} kcal")
    print(f"VET: {dados['vet']} kcal")
    print(f"Calorias Alvo: {macros['vet_alvo']} kcal")
    print(f"Proteínas: {macros['prot_g']}g ({macros['prot_kcal']} kcal)")
    print(f"Carboidratos: {macros['carb_g']}g ({macros['carb_kcal']} kcal)")
    print(f"Gorduras: {macros['gord_g']}g ({macros['gord_kcal']} kcal)")
    print(f"Outras Necessidades: Fibras 25-30g/dia, Água {round(dados['peso'] * 35)}ml/dia")
    print("\nAjustes manuais: Deseja editar? (Implemente se necessário)")

def gerar_plano_dieta(nome, dados):
    """Gera e salva plano de dieta simples."""
    macros = dados['macros']
    divisao = dividir_refeicoes(macros)
    
    print(f"\nPLANO DE DIETA SIMPLES PARA {nome.upper()}")
    print(f"Total Diário: {macros['vet_alvo']} kcal | Prot: {macros['prot_g']}g | Carb: {macros['carb_g']}g | Gord: {macros['gord_g']}g")
    print("Sugestões genéricas - Personalize com preferências e alergias!")
    print("-" * 60)
    
    conteudo = f"PLANO DE DIETA PARA {nome.upper()}\n"
    conteudo += f"Data: {dados['peso']}kg, VET Alvo: {macros['vet_alvo']} kcal\n\n"
    
    for refeicao in divisao:
        print(f"{refeicao['refeicao']}: Prot {refeicao['prot_g']}g | Carb {refeicao['carb_g']}g | Gord {refeicao['gord_g']}g")
       