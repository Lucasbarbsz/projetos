estoque = {"camiseta": 50, "calça": 30, "tenis": 25}

for produto in estoque:
    quantidade = estoque[produto]
    print(produto, quantidade)
    
print('='*40)

print(estoque.items())

print('='*40)

for i,(produto, quantidade) in enumerate(estoque.items(),1):
    print(f'{i}.{produto}: {quantidade} unidades')
    
print('='*40)

for produto, quantidade in estoque.items():
    print(f'{produto}: {quantidade} unidades')

print('='*60)

# Dicionário de temperaturas por cidade
temperaturas = {
    "São Paulo": 22,
    "Rio de Janeiro": 28,
    "Curitiba": 18,
    "Salvador": 30,
    "Porto Alegre": 20
}

# 1. Mostre todas as cidades e temperaturas
print("🌡️ TEMPERATURAS ATUAIS:")
for cidade, temp in temperaturas.items():
    print(f"• {cidade}: {temp}°C")

# 2. Encontre a cidade mais quente
cidade_mais_quente = ""
maior_temp = -100

for cidade, temp in temperaturas.items():
    if temp > maior_temp:
        cidade_mais_quente = cidade
        maior_temp = temp

print(f"\n🔥 Cidade mais quente: {cidade_mais_quente} ({maior_temp}°C)")

# 3. Crie um novo dicionário com cidades abaixo de 25°
frias = {'Rio grande do sul': 19,  
         'Paraná': 20,
         'Goiânia': 27,
}

cidades_frias = {}                                     # cidades_frias → Dicionário VAZIO no começo: {}
                                                       # [cidade] → A CHAVE onde vamos guardar (ex: "Rio grande do sul")
for cidade, temp in frias.items():                     # = → Operador de ATRIBUIÇÃO (guarde isso aqui)
    if temp < 25:                                      # temp → O VALOR que vamos guardar (ex: 19)
        cidades_frias[cidade] = temp

print("Cidades com temperatura abaixo de 25°C:")
print(cidades_frias)