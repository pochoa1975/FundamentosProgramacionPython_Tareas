# función de suma
def suma(operando1, operando2):
    resul_suma = operando1 + operando2
    return resul_suma

resultado = suma(12, 10)

#print(resultado)


# calcular el promedio de temperatura de una ciudad

temperaturas=[
    [ # ciudad
        [# semana
            1, # dia 1
            3, # dia 2
            5  # dia 3
        ],
        [10, 13, 34]
    ],
    [
        [3, 5, 6],
        [5, 6, 7]
    ]
]
def promedio_temp_ciudad(arreglo_temperaturas, ciudad, semana):
    acumulador=0
    for i in range(len(arreglo_temperaturas[ciudad][semana])):
        acumulador = acumulador + arreglo_temperaturas[ciudad][semana][i]

    promedio = acumulador / len(arreglo_temperaturas[ciudad][semana])

    return promedio

resultado_prom = promedio_temp_ciudad(temperaturas, 0, 1)

print(resultado_prom)