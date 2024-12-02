from ProgPrincipal import sacar_tildes

# Verifica que se eliminan las tildes y caracteres especiales
def test_sacar_tildes():
    # Casos con tildes y caracteres especiales
    assert sacar_tildes('áéíóú') == 'aeiou', "Error: No se eliminaron correctamente las tildes."
    assert sacar_tildes('ÁÉÍÓÚ') == 'AEIOU', "Error: No se eliminaron correctamente las tildes en mayúsculas."
    assert sacar_tildes('mañana') == 'manaña', "Error: No se eliminó correctamente la tilde en 'ñ'."
    assert sacar_tildes('Ñandú') == 'Nandu', "Error: No se eliminó correctamente la tilde en 'Ñ'."
    
    # Casos sin tildes, debe devolver el mismo texto
    assert sacar_tildes('hola') == 'hola', "Error: El texto sin tildes no debe cambiar."
    assert sacar_tildes('HOLA') == 'HOLA', "Error: El texto en mayúsculas sin tildes no debe cambiar."
    
    print("Prueba pasada correctamente: La función elimina las tildes y caracteres especiales como se espera.")

# Ejecutar la prueba
test_sacar_tildes()
