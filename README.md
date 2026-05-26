# UTN - Tecnicatura Universitaria en Programación (TUP)
## Cátedra: Organización Empresarial - Año 2026


* Escenario Seleccionado: Escenario D - Estadísticas de Resultados Deportivos.
* Célula de Trabajo (Simulación de Roles): Hugo (Líder / Gobernanza del Repositorio)
  * Paco(Desarrollador Técnico / Lógica y Scripts)
  * Luis (Revisor Técnico / QA y Documentación)

---


Este sistema automatiza el procesamiento de datos de un torneo deportivo. A partir del registro manual de los partidos jugados, calcula la tabla de posiciones oficial bajo el reglamento competitivo tradicional y exporta métricas de rendimiento ofensivo de forma visual.

## Estructura del Repositorio
* `/datos`: Contiene el archivo `resultados_torneo.csv` con el fixture y goles.
* `/scripts`: Alberga el código fuente principal `analisis_deportivo.py`.
* `/resultados`: Espacio donde se exportan las tablas y el gráfico final `rendimiento_equipos.png`.
* `.gitignore`: Filtro de exclusión de archivos temporales del sistema y checkpoints.

## Indicadores Técnicos Calculados
1. Tabla de Posiciones Dinámica: Sumatoria automática de puntos (Victoria = 3 pts, Empate = 1 pt, Derrota = 0 pts).
2. Efectividad Goleadora: Promedio general de goles por partido del campeonato.
3. Métrica Visual: Gráfico de barras comparativo con el rendimiento acumulado de todos los clubes.

## Instrucciones de Ejecución
Para clonar este repositorio y reproducir el análisis de manera local, ejecute:
```bash
git clone [https://github.com/BrunoMat002/Trabajo_Practico_N2.git](https://github.com/BrunoMat002/Trabajo_Practico_N2.git)
cd Trabajo_Practico_N2
python scripts/analisis_deportivo.py
