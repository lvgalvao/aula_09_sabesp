from pydantic import validate_call

@validate_call()
def soma_de_3_parametros(num1: float, num2: float, num3: float) -> float:
    resultado_soma_3_parametros = num1 + num2 + num3
    return resultado_soma_3_parametros

resultado_1 = soma_de_3_parametros(5,5,5)
resultado_2 = soma_de_3_parametros("5","5","5")
print(resultado_1)
print(resultado_2)