'''
Sophia Louise Rodrigues da Luz / RA: 1801130
'''

import salario_funcionario


def teste1_desenvolvedor():
    try:
        lista = []
        lista = ["Sophia Louise, "sophialouiserdl@gmail.com", 3000.00,
                 "DESENVOLVEDOR"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 2400.0
        print("Deu certo!")
    except AssertionError:
        print("Deu errado!")


def teste2_desenvolvedor():
    try:
        lista = []
        lista = ["Sophia Louise", "sophialouiserdl@gmail.com", 2999.00,
                 "DESENVOLVEDOR"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 2667
        print("Deu certo!")
    except AssertionError:
        print("Deu errado!")


def teste1_analista():
    try:
        lista = []
        lista = ["Sophia Louise", "sophialouiserdl@gmail.com", 2000.00,
                 "ANALISTA"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 1700.0
        print("Deu certo!")
    except AssertionError:
        print("Deu errado!")


def teste2_analista():
    try:
        lista = []
        lista = ["Sophia Louise", "sophialouiserdl@gmail.com", 1999.00,
                 "ANALISTA"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 2000
        print("Deu certo!")
    except AssertionError:
        print("Deu errado!")


def teste1_gerente():
    try:
        lista = []
        lista = ["Sophia Louise", "sophialouiserdl@gmail.com, 5000.00,
                 "GERENTE"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 3900.0
        print("Deu certo!")
    except AssertionError:
        print("Deu errado!")


def teste2_gerente():
    try:
        lista = []
        lista = ["Sophia Louise", "sophialouiserdl@gmail.com", 4999.00,
                 "GERENTE"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario == 2119.3333333
        print("Deu certo!")
    except AssertionError:
        print("Deu errado!)


def teste_outro_cargo():
    try:
        lista = []
        lista = ["Sophia Louise", "sophialouiserdl@gmail.com", 4889.00,
                 "Padeiro"]
        salario = salario_funcionario.calcular_salario(lista)
        assert salario > 0
        print("Deu certo!")
    except TypeError:
        print("Deu errado!")


teste1_desenvolvedor()
teste2_desenvolvedor()
teste1_analista()
teste2_analista()
teste1_gerente()
teste2_gerente()
teste_outro_cargo()
