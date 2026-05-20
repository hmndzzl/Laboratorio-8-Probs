import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(2026)

# ── Parameters ───────────────────────────────────────────────────────────────
N = 100    # different stickers
S = 7      # stickers per pack (unique within pack)
R = 10000  # simulations

# ── Simulation ───────────────────────────────────────────────────────────────
packs_results    = []
repeated_results = []

for _ in range(R):
    collected         = np.zeros(N, dtype=bool)
    packs_bought      = 0
    repeated_stickers = 0

    while not collected.all():
        pack = np.random.choice(N, S, replace=False)
        for sticker in pack:
            if collected[sticker]:
                repeated_stickers += 1
            else:
                collected[sticker] = True
        packs_bought += 1

    packs_results.append(packs_bought)
    repeated_results.append(repeated_stickers)

packs_results    = np.array(packs_results)
repeated_results = np.array(repeated_results)

# ── Results ──────────────────────────────────────────────────────────────────
mean_packs    = np.mean(packs_results)
std_packs     = np.std(packs_results)
mean_repeated = np.mean(repeated_results)
std_repeated  = np.std(repeated_results)
p_over_30     = np.mean(packs_results > 30)
theo_min      = math.ceil(N / S)   # = 15

print("=" * 55)
print("RESULTADOS DE LA SIMULACION")
print("=" * 55)
print(f"Media de sobres comprados:          {mean_packs:.4f}")
print(f"Desviacion estandar de sobres:      {std_packs:.4f}")
print(f"Media de figuritas repetidas:       {mean_repeated:.4f}")
print(f"Desviacion estandar de repetidas:   {std_repeated:.4f}")
print(f"P(sobres > 30):                     {p_over_30:.4f}")
print()
print("Justificacion del umbral de 30 sobres:")
print(f"  Minimo teorico: ceil({N}/{S}) = {theo_min} sobres.")
print(f"  30 es el doble del minimo ({theo_min}), lo que representa una")
print(f"  holgura razonable dado el efecto de 'cola larga' del proceso.")
print(f"  La probabilidad P(sobres > 30) = {p_over_30:.4f} cuantifica cuan")
print(f"  frecuente es superar ese doble del minimo.")

# ── Histogram ────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 6))
plt.hist(packs_results, bins=40, edgecolor='black', color='steelblue', alpha=0.7)
plt.axvline(mean_packs, color='red',   linestyle='--', linewidth=2,
            label=f'Media muestral = {mean_packs:.2f}')
plt.axvline(theo_min,   color='green', linestyle='-',  linewidth=2,
            label=f'Minimo teorico = {theo_min}')
plt.title(f'Distribucion del numero de sobres para completar el album\n'
          f'(N={N}, S={S}, R={R:,} simulaciones)')
plt.xlabel('Numero de sobres comprados')
plt.ylabel('Frecuencia')
plt.legend()
plt.tight_layout()
plt.savefig('distribucion_sobres.png', dpi=150)
plt.show()

# ── Analysis Questions ────────────────────────────────────────────────────────
print()
print("=" * 55)
print("ANALISIS")
print("=" * 55)

# Q1 — Minimum packs without repeats
print()
print("Pregunta 1: Minimo de sobres sin figuritas repetidas")
print("-" * 55)
print(f"  Si ninguna figurita se repitiera, cada sobre aportaria")
print(f"  exactamente S={S} figuritas nuevas. Para N={N} figuritas:")
print(f"    Minimo = ceil(N/S) = ceil({N}/{S}) = ceil({N/S:.6f}) = {theo_min} sobres")
min_count = int(np.sum(packs_results == theo_min))
print(f"  Apariciones en simulaciones: {min_count} de {R} ({100*min_count/R:.4f}%).")
if min_count == 0:
    print(f"  No se observo este caso: la probabilidad es extremadamente")
    print(f"  pequenya; siempre hay al menos alguna repeticion en la practica.")
else:
    print(f"  Se observo {min_count} vez/veces -- evento muy raro.")

# Q2 — Harmonic number approximation
print()
print("Pregunta 2: Calculo teorico con H_100")
print("-" * 55)
H_N = np.log(N) + 0.5772
E_T = (N / S) * H_N
print(f"  H_100 aprox ln(100) + 0.5772")
print(f"        = {np.log(N):.4f} + 0.5772")
print(f"        = {H_N:.4f}")
print(f"  E[T]  = (N/S) * H_100")
print(f"        = ({N}/{S}) * {H_N:.4f}")
print(f"        = {N/S:.4f} * {H_N:.4f}")
print(f"        = {E_T:.4f} sobres")
print(f"  Media simulada: {mean_packs:.4f} sobres")
diff_pct = 100 * abs(E_T - mean_packs) / mean_packs
print(f"  Diferencia absoluta: {abs(E_T - mean_packs):.4f} sobres ({diff_pct:.2f}%)")
print(f"  La aproximacion es {'muy cercana' if diff_pct < 5 else 'razonable'} a la media simulada.")

# Q3 — Theoretical repeated stickers
print()
print("Pregunta 3: Figuritas repetidas -- teorico vs simulado")
print("-" * 55)
E_repeated = E_T * S - N
print(f"  Total de figuritas abiertas aprox E[sobres] * S")
print(f"    = {E_T:.4f} * {S} = {E_T*S:.4f}")
print(f"  De esas, N={N} son nuevas (para completar el album).")
print(f"  E[repetidas] = E[sobres] * S - N = {E_T*S:.4f} - {N} = {E_repeated:.4f}")
print(f"  Media simulada de repetidas: {mean_repeated:.4f}")
print(f"  Diferencia: {abs(E_repeated - mean_repeated):.4f} figuritas")

# Q4 — Variability interpretation
print()
print("Pregunta 4: Interpretacion de la desviacion estandar")
print("-" * 55)
cv = std_packs / mean_packs
print(f"  Media:                 {mean_packs:.4f} sobres")
print(f"  Desviacion estandar:   {std_packs:.4f} sobres")
print(f"  Coeficiente de var.:   {cv:.4f}  ({100*cv:.2f}%)")
print()
print(f"  La desviacion es {'ALTA' if cv > 0.25 else 'moderada'} relativa a la media (CV aprox {100*cv:.1f}%).")
print("  Esto refleja el efecto de 'cola larga' del coleccionismo:")
print("  - Las primeras figuritas son faciles de obtener.")
print("  - Las ultimas son muy dificiles (pocas chances de salir).")
print("  - Este desequilibrio genera asimetria positiva y alta varianza.")
print("  - No hay control sobre que sale en cada sobre: la suerte")
print("    domina y algunos terminan rapido mientras otros tardan mucho.")
