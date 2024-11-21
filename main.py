from typing import List
from pydantic import validate_call

temperatura_celsius = [0, 20, 100]

@validate_call
def conversor(lista_temp_celsius: List[float]) -> List[float]:
    """
    Função que converte temperaturas de Celsius para Fah
    """
    lista_temp_fah = []
    for temp_celsius in lista_temp_celsius:
        temp_fah = (temp_celsius * 9/5) + 32
        lista_temp_fah.append(temp_fah)
    return lista_temp_fah

temperatura_convertida = conversor([0, 20, "Marcelo", 500])

print(temperatura_convertida)