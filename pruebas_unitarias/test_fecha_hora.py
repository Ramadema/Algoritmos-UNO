from ProgPrincipal import generar_fecha_hora
from datetime import datetime, timedelta

# Verifica que el formato de la fecha sea correcto
fecha, hora = generar_fecha_hora()
assert len(fecha) == 10, f"Error: La fecha debe tener 10 caracteres, pero tiene {len(fecha)}"
assert len(hora) == 5, f"Error: La hora debe tener 5 caracteres, pero tiene {len(hora)}"
assert fecha.count('-') == 2, f"Error: La fecha debe tener 2 guiones, pero tiene {fecha.count('-')}"

# Verifica que la fecha esté dentro de los próximos 30 días
fecha_actual = datetime.now()
fecha_generada = datetime.strptime(fecha, "%Y-%m-%d")
assert fecha_generada >= fecha_actual, f"Error: La fecha generada ({fecha_generada}) es anterior a la actual ({fecha_actual})"
assert fecha_generada <= fecha_actual + timedelta(days=30), f"Error: La fecha generada ({fecha_generada}) está más allá de los próximos 30 días"

# Verifica que la hora esté en el rango 00:00 a 23:59
hora_generada = datetime.strptime(hora, "%H:%M")
assert 0 <= hora_generada.hour <= 23, f"Error: La hora generada ({hora_generada}) está fuera del rango de horas (00-23)"
assert 0 <= hora_generada.minute <= 59, f"Error: Los minutos generados ({hora_generada.minute}) están fuera del rango de minutos (00-59)"

print("Todas las pruebas pasaron correctamente.")
