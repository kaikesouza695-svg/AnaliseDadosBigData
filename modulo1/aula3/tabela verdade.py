
#### contexto1 

'''''
para que eu possa dirgir, eu preciso ter:
-ter cnh
-ser +18 anos
-comsumiu bebida alcoolica
'''

pergunta1 = input("tem cnh?")
pergunta2 = int(input("qual a sua idade?"))
pergunta3 = input("você consumiu bebida alcoolica?")

if pergunta1 == "sim" and pergunta2 >= 18:
    print("pode dirgir")
elif pergunta1 == "sim" and pergunta3 == "sim":
    print("não pode dirgir.")


   #contexto2

''''
pra me deslocar para o senac nova iguaço, posso utilizar;
- trem;
-ônibus;
-metro.
'''

trem = input("vc veio de trem?")
ônibus = input("vc veio de ônibus?")
metro = input ("vc veio de metro?")

if trem == "sim" or ônibus == "sim" or metro =="sim":
    print("bem vindo ao senac")
else:
    print("tarifa dinâmica, né? :()")