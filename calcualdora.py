# calculadora.py
# Cambiá los valores y agregá una operación más al final

num1 = 5  # cambiá este valor
num2 = 9   # cambiá este valor

print(f"Suma:           {num1} + {num2} = {num1 + num2}")
print(f"Resta:          {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} x {num2} = {num1 * num2}")

# Agregá acá una operación más — división, módulo, potencia, lo que quieras

print(f"División:       {num1} / {num2} = {num1 / num2}")

if num2 != 0:
    print(f'División: {num1} / {num2} = {num1 / num2}')
else:
    print('División: no se puede dividir por cero')