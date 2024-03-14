# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#                                       C = 5 * ((F-32) / 9).
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print(f"\tConversor de temperatura.")




def celsius_to_fahrenheit():
    temp = float(input("Digite a temperatura em celsius: "))
    return((temp * 9/5) + 32)
def fahrenheit_to_celsius():
    temp = float(input("Digite a temperatura fahrenheit: "))
    return(5 * ((temp-32) / 9))
while True:
  try:    
      choice = input(f"\nDesejar transformar uma temperatura em celsius(c) ou fahrenheit(f)? ")
      if choice == "c":
        print(f"\n\tA temperatura em fahrenheit é {celsius_to_fahrenheit():.2f}°F")
        break
      elif choice == "f":
        print(f"\n\tA temperatura em celsius é:  {fahrenheit_to_celsius():.2f}°C")
        break
      else:
        print("Por favor, escolha 'c' para Celsius ou 'f' para Fahrenheit.")
  except ValueError:
      print("Temperatura Inválida!")

