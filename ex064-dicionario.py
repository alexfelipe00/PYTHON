pessoas = {'nome': 'Alex', 'idade': '24', 'sexo': 'M'}
print(pessoas)

print(f"O {pessoas['nome']} do sexo {pessoas['sexo']} tem {pessoas['idade']} anos de idade")

del pessoas['sexo']
pessoas['nome'] = 'Marcio'

pessoas['peso'] = 71

print(f"{pessoas.keys()}")
print(f"{pessoas.values()}")
print(f"{pessoas.items()}")

for k in pessoas.keys():
    print(f"{k}")

for k, v in pessoas.items():
    print(f"{k} = {v}")