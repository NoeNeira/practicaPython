"""
Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito. 
Evaluar si puede realizar una compra de $2500, si puede indicar cuánto saldo 
le queda luego de efectuarla. Si no puede, indicar cuánto dinero le falta para poder realizarla.
"""

montoTarjeta = int(input("Ingrese el monto: "))
valorCompra = 2500

if montoTarjeta >= 2500:
    print(f"Su saldo es de ${montoTarjeta - 2500}")
else:
    saldo = 2500 - montoTarjeta
    print(f"Le faltan ${saldo}. No tiene saldo suficiente para realizar la compra")
    
