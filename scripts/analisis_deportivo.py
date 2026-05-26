import pandas as pd
import matplotlib.pyplot as plt

# Importamos el dataset utilizando rutas relativas para garantizar reproducibilidad
# Esto permite que cualquier integrante corra el proyecto sin fallos de rutas absolutas
df = pd.read_csv("datos/resultados_torneo.csv")

#Generamos un diccionario para estructurar la información procesada de los clubes
# Guardará de forma dinámica: partidos ganados, goles anotados y puntos acumulados
equipos = {}

def inicializar_equipo(eq):
    "Inicializa las métricas de un equipo si no fue procesado previamente."
    if eq not in equipos:
        equipos[eq] = {"ganados": 0, "goles": 0, "puntos": 0}

# Procesamos el fixture y utilizamos la siguinete lógica para la asignación de puntos
# Victoria: 3 puntos | Empate: 1 punto | Derrota: 0 puntos
for _, fila in df.iterrows():
    loc, vis = fila["local"], fila["visitante"]
    g_loc, g_vis = int(fila["goles_local"]), int(fila["goles_visitante"])
    
    # Aseguramos que ambos clubes existan en nuestra estructura de datos
    inicializar_equipo(loc)
    inicializar_equipo(vis)
    
    # Acumulación de goles a favor
    equipos[loc]["goles"] += g_loc
    equipos[vis]["goles"] += g_vis
    
    # Evaluación del resultado del partido para determinar el puntaje
    if g_loc > g_vis:
        equipos[loc]["ganados"] += 1
        equipos[loc]["puntos"] += 3
    elif g_vis > g_loc:
        equipos[vis]["ganados"] += 1
        equipos[vis]["puntos"] += 3
    else:
        equipos[loc]["puntos"] += 1
        equipos[vis]["puntos"] += 1

# Convertimos el diccionario a DataFrame para manipular y ordenar los resultados
df_posiciones = pd.DataFrame.from_dict(equipos, orient='index').sort_values(by='puntos', ascending=False)

print("=== TABLA DE POSICIONES ===")
print(df_posiciones[["puntos", "ganados"]])
print("\n===========================")

# Cálculamos las métricas globales del torneo
total_goles = df["goles_local"].sum() + df["goles_visitante"].sum()
promedio_goles = total_goles / len(df)
print(f"Promedio de goles por partido en el torneo: {promedio_goles:.2f}\n")

# Generación del gráfico comparativo de rendimiento técnico
# Se utiliza un gráfico de barras para contrastar de forma visual la efectividad de los equipos
plt.figure(figsize=(7, 4))
plt.bar(df_posiciones.index, df_posiciones["puntos"], color=["navy", "darkred", "skyblue", "red"])
plt.title("Rendimiento del Campeonato - Puntos Totales")
plt.xlabel("Equipos")
plt.ylabel("Puntos")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Guardado automático en la carpeta /resultados para la posterior auditoría de QA
plt.savefig("resultados/rendimiento_equipos.png")
print("Análisis deportivo completado de forma exitosa. Gráfico exportado.")
