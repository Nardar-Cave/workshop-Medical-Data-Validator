# Declare uma variável chamada medical_records e atribua a ela uma lista vazia. 
# Nos passos seguintes, você vai usá-lo para armazenar seus dados médicos.

'''medical_records = []'''

# A lista medical_records armazenará dicionários, cada um deles representando um paciente. 
# Adicione um dicionário com a chave patient_id e valor da string P1001 à lista medical_records.

'''medical_records = [
    {
        'patient_id': 'P1001'
    }    
]'''


# Adicione uma chave age com o valor do inteiro 34 e uma chave gender com o valor da string Female ao seu dicionário. 
# Não esqueça da vírgula entre os pares chave-valor.

'''medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female'
    }    
]'''

# Complete o dicionário adicionando os seguintes três pares chave-valor:
# Uma chave diagnosis com o valor de Hypertension
# Uma chave medications com o valor da lista ['Lisinopril']
# Uma chave last_visit_id com o valor de V2301.

'''medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }    
]'''


# Seguindo a mesma estrutura que você usou nas etapas anteriores, a lista medical_records foi preenchida para você com os dados de outros pacientes. 
# Fique à vontade para dar uma olhada.
# A seguir você começará a escrever a função para validar o conjunto de dados. 
# Crie uma função chamada validate com um único parâmetro data.
# Você quer garantir que seus dados sejam uma lista ou uma tupla. 
# Portanto, dentro da função validate, declare uma variável chamada is_sequence e atribua a ela uma chamada para isinstance. 
# Passe data como o primeiro argumento e uma tupla contendo list e tuple como o segundo argumento.



medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }, 
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    }, 
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    }, 
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]



def validate(data):
    is_sequence = isinstance(data, (list, tuple))

# Crie uma declaração if. 
# Para sua condição, use o operador not para negar is_sequence. 
# Dentro da declaração if, imprima Invalid format: expected a list or tuple. 
# e retorne False.

    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False

# Logo após sua declaração if, declare uma variável chamada is_invalid e defina-a como False. 
# Mais tarde, você usará isso como uma flag para executar uma instrução condicional.

    is_invalid = False

# Crie um loop for que itere sobre data. 
# Use a função enumerate para obter tanto o índice quanto o item em data a cada iteração. 
# Use index e dictionary como variáveis de iteração.
# Por enquanto use pass para preencher o corpo do loop.

   ''' for index, dictionary in enumerate(data):
        pass'''

# Dentro do seu loop for, se o item em dictionary não for uma instância de dict, imprima Invalid format: expected a dictionary at position <index>. 
# (onde <index> deve ser substituído pelo índice atual) e defina is_invalid como True.

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

# Após seu loop for, ainda dentro da função validate, crie uma declaração if. Se is_invalid for True, retorne False.

    if is_invalid == True:
        return False

# Após a declaração if, imprima a string Valid format.. Então retorne True.

    print("Valid format.")
    return True

# Na parte inferior do seu código, chame a função validate com medical_records como argumento. 
# Você deve ver Valid format. impresso no terminal.

validate(medical_records)

# Dentro da função validate, use o construtor set() para criar um conjunto a partir da seguinte lista de chaves que cada dicionário deve ter: 
# ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']. 
# Atribua o conjunto a uma variável chamada key_set.

    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])


# Dentro do seu loop for, após a primeira instrução if, crie uma instrução if que execute quando o conjunto de chaves do dicionário atual for diferente de key_set. 
# Isto é para garantir que não haja chaves ausentes ou inválidas no dicionário.
# Dentro da nova declaração if, imprima Invalid format: <dictionary> at position <index> has missing and/or invalid keys. 
# (onde <dictionary> e <index> devem ser substituídos pelo dicionário e índice na iteração atual) e defina is_invalid como True.

        if set(dictionary.keys()) != key_set:
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True

# Agora você vai tornar a validação mais granular. 
# Crie uma função chamada find_invalid_records para encontrar valores inválidos em um dicionário. 
# Forneça os seguintes parâmetros: patient_id, age, gender, diagnosis, medications e last_visit_id.
# Dentro da sua nova função, crie um dicionário vazio chamado constraints. 
# Então, retorne constraints da sua nova função.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = dict()
    return constraints'''


# Na parte inferior do seu código, imprima o resultado da chamada da função find_invalid_records. 
# Para seus argumentos, use o operador ** para desempacotar medical_records[0].

print(find_invalid_records(**medical_records[0]))


# O dicionário constraints conterá cada chave que você deve esperar ter nos dados para validar.
# O valor associado a cada um deles indicará o resultado da validação.
# Adicione a chave patient_id ao dicionário constraints. 
# Para seu valor, use uma chamada para isinstance passando patient_id e str como argumentos.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str)
    }'''

# Como você escreveu na etapa anterior, patient_id deve ser uma string. 
# Você quer verificar se ele também possui um padrão específico, porém.
# Para isso, você vai usar uma expressão regular.
# Portanto, no início do seu código, use a palavra-chave import para importar o módulo re.

import re

# Chame re.search com a string p como primeiro argumento e patient_id como segundo argumento. 
# Use o operador and para adicionar a chamada da função como uma segunda expressão ao valor da sua chave patient_id.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
        constraints = {
            'patient_id': isinstance(patient_id, str) and re.search('p', patient_id)
    }'''

# Adicione re.IGNORECASE como o terceiro argumento na sua chamada re.search. 
# Isso fará com que sua busca com regex não diferencie maiúsculas de minúsculas.
# Depois disso, você verá None substituído pelo objeto de correspondência <re.Match object; span=(0, 1), match='P'>, onde match indica a correspondência e span indica sua localização na string.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {'patient_id': isinstance(patient_id, str) and re.search('p', patient_id, re.IGNORECASE)
    }'''

# Após a letra p, patient_id deve conter uma série de números. 
# Então, modifique seu padrão regex para ter o caractere p seguido da sequência especial \d.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.search('p\d', patient_id, re.IGNORECASE)
    }'''

# Então adicione um quantificador + ao seu padrão regex para corresponder a um ou mais dígitos.


'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
constraints = {
    'patient_id': isinstance(patient_id, str) and re.search('p\d+', patient_id, re.IGNORECASE)
    }'''

# Substitua a chamada search por uma chamada fullmatch mantendo os mesmos argumentos.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE)
    }'''

# Em seguida, você quer verificar se age é um inteiro. 
# Então adicione outra chave age ao dicionário constraints. 
# Para seu valor, chame isinstance passando age e int como seus argumentos.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int)
    }'''

# age não deve ser apenas um inteiro, deve ser um inteiro positivo maior ou igual a 18.
# Usando o operador and, adicione uma segunda expressão ao valor da chave age para verificar isso.

'''def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18'''

# Adicione outra chave gender ao dicionário constraints.
# Seguindo o formato da expressão que você escreveu nos passos anteriores, verifique se gender é uma string. 
# Então, use o operador and para verificar se o gender em minúsculas está em ('male', 'female').

        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female')

# Agora adicione uma chave diagnosis ao dicionário constraints.
# Para seu valor, escreva uma expressão que verifique se diagnosis é uma instância de str ou é None.

        'diagnosis' : isinstance(diagnosis, str) or diagnosis is None

# Em seguida, adicione uma chave medications ao dicionário constraints.
# Para seu valor use isinstance para verificar se medications é uma lista.

        'medications':  isinstance(medications, list)
    
# Passe a lista [isinstance(i, str) for i in medications] para a função all para garantir que cada elemento nela seja uma string.

        'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications]) 

# Adicione uma última chave last_visit_id ao dicionário constraints. 
# Para seu valor, use isinstance para verificar se last_visit_id é uma string.        

        'last_visit_id': isinstance(last_visit_id, str)

# É hora de usar outra expressão regular.
# De forma semelhante ao que você já fez, use o operador and para adicionar uma expressão ao valor atual de constraints['last_visit_id'].
# No lado direito do operador and, use a função fullmatch do módulo re para garantir que last_visit_id comece com a letra v (minúscula ou maiúscula) seguida por um ou mais dígitos.

        'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)

# Agora que seu dicionário constraints está completo, você vai alterar a declaração return de find_invalid_records para que ela retorne uma lista das chaves inválidas.
# Usando a sintaxe de list comprehension, retorne uma lista que avalie key para cada key, value em constraints.items().
# Como você quer retornar uma lista contendo apenas chaves inválidas, adicione uma cláusula if à sua compreensão para que cada key seja adicionada à lista somente quando value for falsy.

    return [key for key, value in constraints.items() if not value]   

# A função find_invalid_records está completa. Agora, remova print(find_invalid_records(**medical_records[0])) do seu código.
# Voltando para a função validate, após as duas declarações if e ainda dentro do loop for, crie uma variável chamada invalid_records.
# Então, atribua a ela uma chamada para find_invalid_records usando o operador ** para desempacotar dictionary.

        invalid_records = find_invalid_records(**dictionary)    


# If you pass invalid data to the validate function, for example a list containing non-dictionary elements or dictionaries with missing and/or invalid keys, Python will raise an AttributeError and a TypeError, respectively. 
# Feel free to verify it by modifying the medical_records list.
# To avoid that, after setting is_invalid to True, use the continue keyword to skip to the next iteration in both your if statements.

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

# Right after the invalid_records variable, create a for loop to iterate over it. 
# For each invalid record, print Unexpected format '<key>: <val>' at position <index>.. 
# Replace <key>, <val>, and <index> with the current key, value, and index.
# Remember that invalid_records is a list of keys that refer to invalid records in the current dictionary. 
# You will need to take the key from invalid_records and look up the value in dictionary.
# Position or index refers to the current dictionary in medical_records, defined by the outer for loop in the function.
# Review your code so far if you need to remind yourself of the loops and variables already created.
# Then, set is_invalid to True.
# Feel free to test the validate function with invalid data to see the validation messages.
# With that, the medical validator workshop is complete.

        for key in invalid_records: 
            val = dictionary[key]               
            print(f"Unexpected format '{key}: {val}' at position {index}.")
            is_invalid = True