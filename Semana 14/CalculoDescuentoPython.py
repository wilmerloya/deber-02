def calcular_descuento(monto_total, porcentaje_descuento=15):
    # Calcular el descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función con solo el monto total
    monto1 = 324.0  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)  # Usa el descuento predeterminado (15%)
    monto_final1 = monto1 - descuento1

    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f} (15%)")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 324.0  # Otro monto total de la compra
    porcentaje_descuento2 = 9  # Un 9% de descuento
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    monto_final2 = monto2 - descuento2

    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f} (9%)")
    print(f"Monto final a pagar: ${monto_final2:.2f}")
