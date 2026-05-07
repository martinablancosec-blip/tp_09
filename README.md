# Temperature Monitor

Aplicación simple en Python para monitorear la temperatura de un equipo industrial.

## Funcionalidades

- Detecta sobrecalentamiento
- Genera alarma si la temperatura supera los 80°C
- Valida errores de sensor

## Reglas del sistema

- Temperatura > 80°C → ALARMA
- Temperatura <= 80°C → NORMAL
- Temperaturas negativas → Error de lectura

## Archivos

- `main.py` → ejecución principal
- `temperature.py` → lógica del sistema
- `tests/` → pruebas automáticas

## Autor

Proyecto realizado con Git y GitHub.