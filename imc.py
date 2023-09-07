def message_imc(IMC: float) -> str:
    if IMC<16.5:
        msg = ("Dénutrition ou famine")
    elif IMC<=18.5:
        msg=("maigreur")
    elif IMC<=25:
        msg=("corpulence normale")  
    elif IMC<=30:
        msg=("surpoid")
    elif IMC<=35:
        msg=("Obésité modérée")
    elif IMC<40:
        msg=("Obésité sévère")
    else :
        msg=("Obésité morbide")
    return msg

poids = float(input('Entrer votre IMC : '))
message = message_imc(poids)
print (message)

