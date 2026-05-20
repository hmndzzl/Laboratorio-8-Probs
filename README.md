# ⚽🃏 Simulación Monte Carlo: Álbum de Figuritas (Laboratorio 7)

**MM3014 · Teoría de Probabilidades | Universidad del Valle de Guatemala (UVG)**  
**Integrantes:**  
* 👤 **Javier Alvarado** - Carné 24546  
* 👤 **Hugo Méndez** - Carné 241265  

---

## 📝 Descripción del Proyecto

Este repositorio contiene la implementación y el análisis de una **Simulación de Monte Carlo** para modelar el proceso de completar un álbum de figuritas coleccionables. El estudio se divide en dos etapas principales y está disponible tanto en formato interactivo (**Jupyter Notebook**: `lab7.ipynb`) como en un script de Python ejecutable (**Script**: `lab7.py`).

### Parámetros del Problema
* **$N = 100$**: Total de figuritas distintas que componen el álbum.
* **$S = 7$**: Figuritas por sobre. Es muy importante destacar que las figuritas dentro de un mismo sobre son **únicas** (muestreo sin reemplazo al abrir un sobre).
* **$R = 10,000$**: Número de simulaciones independientes realizadas para asegurar la convergencia estadística (Estabilidad de Monte Carlo).

---

## 🛠️ Metodología de la Simulación

La simulación modela la compra secuencial de sobres hasta que se marca como "adquirida" cada una de las $N=100$ figuritas. Para cada una de las $10,000$ repeticiones:
1. Se inicializa un vector booleano de tamaño $100$ en `False` (álbum vacío).
2. Se genera un ciclo que simula la compra de un sobre usando un muestreo aleatorio sin reemplazo (`np.random.choice(N, S, replace=False)`), garantizando que las $S=7$ figuritas dentro del sobre sean distintas.
3. Se actualiza el álbum y se contabilizan las figuritas repetidas (aquellas que ya habían sido marcadas como `True`).
4. El ciclo se detiene cuando todas las posiciones del vector son `True` (álbum completo).
5. Se registran la cantidad de sobres totales comprados y la cantidad de figuritas repetidas obtenidas.

---

## 📊 Resultados Generales (Etapa 1)

Los resultados obtenidos mediante la simulación de Monte Carlo se comparan con las aproximaciones teóricas derivadas de la **Teoría del Coleccionista de Cupones** (*Coupon Collector's Problem*):

| Métrica | Valor Teórico (Aproximado) | Valor Simulado (Promedio) | Diferencia Absoluta / Error Relativo |
| :--- | :---: | :---: | :---: |
| **Sobres para completar ($E[T]$)** | $74.0348$ sobres (usando $H_{100}$) | **$72.2456$ sobres** | $1.7892$ sobres ($2.47\%$) |
| **Figuritas repetidas ($E[R]$)** | $418.2439$ figuritas | **$405.7192$ figuritas** | $12.5247$ figuritas ($3.08\%$) |
| **Mínimo teórico de sobres** | $15$ sobres ($\lceil 100/7 \rceil$) | **$15$ sobres** | $0.00\%$ (No observado en la simulación) |
| **Desviación estándar de sobres ($\sigma$)** | *N/A* | **$17.4715$ sobres** | *N/A* ($CV \approx 24.18\%$) |
| **Probabilidad de requerir $>30$ sobres** | $\approx 1.0000$ | **$1.0000$ (100%)** | $0.00\%$ |

> [!NOTE]
> La aproximación teórica utiliza el **Número Armónico $H_{100} \approx \ln(100) + 0.5772 \approx 5.1824$**. La fórmula para el valor esperado de sobres es $E[T] = \frac{N}{S} H_N$. La excelente coincidencia con los datos empíricos valida la precisión del modelo de simulación.

---

## 📈 Explicación Detallada de las Gráficas

Las simulaciones generan dos visualizaciones clave que describen detalladamente el comportamiento probabilístico del problema.

### 1. Distribución del Número de Sobres (`distribucion_sobres.png`)
Esta gráfica muestra la frecuencia (o probabilidad empírica) del número de sobres necesarios para completar el álbum a lo largo de las $10,000$ ejecuciones.

* **Eje X (Horizontal - Número de sobres comprados):** Representa la cantidad de sobres que le tomó a un coleccionista completar el álbum.
* **Eje Y (Vertical - Frecuencia):** Indica en cuántas de las $10,000$ simulaciones se requirió exactamente esa cantidad de sobres.
* **Línea Roja Discontinua (Media Muestral $\approx 72.25$ sobres):** Muestra el promedio de sobres necesarios.
* **Línea Verde Continua (Mínimo Teórico $= 15$ sobres):** El escenario utópico en el que nunca sale una sola figurita repetida. Nótese que la probabilidad de lograr esto es prácticamente cero; en las 10,000 simulaciones **ningún** caso logró completarse en 15 sobres.
* **Análisis de la Forma:** La distribución presenta una marcada **asimetría positiva (sesgo a la derecha)**. Esto ilustra el clásico fenómeno de la "cola larga" (*long-tail*): es sumamente fácil conseguir las primeras figuritas, pero las últimas requieren abrir decenas de sobres debido a la bajísima probabilidad de obtener justamente las faltantes. Algunos coleccionistas con "mala suerte" requirieron más de $120$ sobres.

<img width="1500" height="900" alt="image" src="https://github.com/user-attachments/assets/73572bec-846d-4240-b474-0d646ee4e2ba" />

---

### 2. Probabilidad de Éxito en función del Presupuesto (`probabilidad_completar.png`)
Esta gráfica de barras representa la probabilidad acumulada de haber completado el álbum tras comprar una cantidad fija $M$ de sobres.


* **Eje X (Horizontal - Sobres Comprados $M$):** Hitos discretos de sobres evaluados ($20, 25, 30, \dots, 80$).
* **Eje Y (Vertical - Probabilidad de Éxito):** La probabilidad empírica $P(\text{Completar} \mid M \text{ sobres})$.
* **Línea Roja Discontinua (Umbral del 50%):** Marca la probabilidad de "moneda al aire" (50% de probabilidad de éxito).
* **Análisis de las Barras:**
  * Para **$M \le 30$ sobres**, la probabilidad de completar el álbum es **prácticamente $0\%$**. Comprar el doble del mínimo teórico sigue siendo insuficiente.
  * Para **$M = 50$ sobres**, la probabilidad de éxito es muy baja, de apenas **$5.63\%$**.
  * El umbral de la mitad de probabilidad (50%) se supera por primera vez a los **$70$ sobres** (alcanzando un **$53.36\%$**).
  * A los **$80$ sobres**, un coleccionista tiene un **$73.26\%$** de probabilidad de haber terminado su álbum.

<img width="1500" height="900" alt="image" src="https://github.com/user-attachments/assets/ceb7c7fb-9843-41cc-9917-9c1fd8f3f2ac" />

---

## 🔍 Análisis Profundo (Etapa 2)

### 1. Relación entre la Mediana y el Hito de Éxito
La **mediana muestral** calculada en la simulación es de **$69$ sobres**. Por definición, la mediana es el valor que acumula exactamente el $50\%$ de la probabilidad. 
Como los hitos evaluados en la Etapa 2 se incrementan de forma discreta, **$M = 70$** es el primer valor evaluado que es mayor o igual a la mediana. Por ende, es matemáticamente consistente que $M = 70$ sea el primer hito en superar el umbral del $50\%$ de éxito ($53.36\%$).

### 2. Cota de la Unión para $M = 50$
La **Cota de la Unión** (*Union Bound*) nos provee un límite superior teórico para la probabilidad de fracaso (es decir, la probabilidad de que al menos una figurita quede sin colectar después de abrir $M$ sobres):

$$P(\text{Fracaso}) \le N \cdot e^{-\frac{M \cdot S}{N}}$$

Para un presupuesto de **$M = 50$** sobres:
* **Probabilidad de fracaso simulada:** $1 - P(\text{Éxito}) = 1 - 0.0563 = 0.9437$ ($94.37\%$).
* **Cota de la Unión teórica:** 
  $$100 \cdot e^{-\frac{50 \cdot 7}{100}} = 100 \cdot e^{-3.5} \approx 3.0197 \text{ (o } 301.97\% \text{)}$$

> [!WARNING]
> **Evaluación de Utilidad de la Cota:**  
> En este escenario, la Cota de la Unión **no es útil**. Debido a que cualquier probabilidad está acotada superiormente por $1$ ($100\%$) de forma trivial, una cota superior de $3.0197$ no aporta información relevante. 
>
> La Cota de la Unión asume que los eventos de que falte cada estampa individual son disjuntos (no se traslapan), lo cual es una pésima aproximación cuando $M$ es pequeño y las intersecciones de figuritas faltantes son muy grandes. Esta cota solo se vuelve matemáticamente útil (menor a $1$) cuando $M > \frac{N \ln(N)}{S}$, es decir, a partir de **$M = 66$ sobres**.

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos Previos
Asegúrate de tener instalado Python y las bibliotecas necesarias:
```bash
pip install numpy matplotlib
```

### Opción 1: Ejecutar el Script interactivo (Jupyter Notebook)
Abre el notebook para visualizar de forma interactiva la ejecución celda por celda y la generación dinámica de gráficos:
```bash
jupyter notebook lab7.ipynb
```

### Opción 2: Ejecutar el Script de Consola (Python)
Para realizar la simulación y guardar las gráficas en formato `.png` de forma directa, ejecuta el archivo de Python:
```bash
python lab7.py
```
El script imprimirá el análisis detallado y las respuestas a las preguntas directamente en la consola, y actualizará las imágenes en el directorio de trabajo.
