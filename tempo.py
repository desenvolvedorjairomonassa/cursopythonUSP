segundos = input("Por favor, entre com o número de segundos que deseja converter:")
dias = int(segundos)//86400
segundosrestantes = int(segundos)%86400
horas = segundosrestantes//3600
segundosrestantes = segundosrestantes%3600
minutos = segundosrestantes//60
segundos = segundosrestantes%60
print(dias, "dias,", horas, "horas,", minutos, "minutos e",segundos , "segundos.")
