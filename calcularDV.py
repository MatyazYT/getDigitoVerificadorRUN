rut = raw_input("Ingresa tu RUT sin el digito verificador: ")

if len(rut) > 8 or len(rut) < 7:
    print "RUT Incorrecto."
    raw_input()
    exit()

splitrut = list(rut)

rut1 = int(splitrut[-1]) * 2
rut2 = int(splitrut[-2]) * 3
rut3 = int(splitrut[-3]) * 4
rut4 = int(splitrut[-4]) * 5
rut5 = int(splitrut[-5]) * 6
rut6 = int(splitrut[-6]) * 7
rut7 = int(splitrut[-7]) * 2
try:
    rut8 = int(splitrut[-8]) * 3
    result = rut1 + rut2 + rut3 + rut4 + rut5 + rut6 + rut7 + rut8
    step2 = int(result) / 11
    step3 = step2 * 11
    step4 = result - step3
    step5 = 11 - step4
    if step5 == 11:
        step5 = 0
    elif step5 == 10:
        step5 = "K"
    final = rut + "-" + str(step5)
    print final
except IndexError:
    result = rut1 + rut2 + rut3 + rut4 + rut5 + rut6 + rut7
    step2 = int(result) / 11
    step3 = step2 * 11
    step4 = result - step3
    step5 = 11 - step4
    if step5 == 11:
        step5 = 0
    elif step5 == 10:
        step5 = "K"
    final = rut + "-" + str(step5)
    print final
