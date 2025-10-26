from functools import reduce
from typing import List, Dict, Any, Generator

# 1. Dati di Partenza
GIOCATORI_BASE: List[Dict[str, Any]] = [
    {'nome': 'Eroe', 'livello': 5, 'punti': 1500},
    {'nome': 'Guerriero', 'livello': 12, 'punti': 8000},
    {'nome': 'Ladro', 'livello': 5, 'punti': 1200},
    {'nome': 'Mago', 'livello': 2, 'punti': 300},
    {'nome': 'Errato', 'livello': 1, 'punti': -500},  # Invalido: punti negativi
    {'nome': 'Erratissimo', 'livello': 1},  # Invalido: mancano i punti
]


PUNTEGGIO_MINIMO_QUALIFICAZIONE = 2000

print(f"--- 1. Dati di Partenza ---")
print(GIOCATORI_BASE)
print("-" * 30)


# ====================================================================
# Task A: Mappa/Generatore
# Calcola il Punteggio Totale: Punti Base + (Livello * 100)
# ====================================================================

def calcola_punteggio_totale_generatore(giocatori: List[Dict[str, Any]]) -> Generator[Dict[str, Any], None, None]:
    punti_base=GIOCATORI_BASE.get('punti')
    livello=GIOCATORI_BASE.get('livello')
    for el in punti_base:
        
    

# Otteniamo un generatore (non ancora eseguito)
giocatori_con_totale_gen = calcola_punteggio_totale_generatore(GIOCATORI_BASE)

# Convertiamo in lista per le fasi successive (forza l'esecuzione del generatore)
giocatori_con_totale = list(giocatori_con_totale_gen)

print("\n--- 2. Risultato Mappa/Generatore (e gestione 'raise') ---")
print("Dopo calcolo Punti Totali e rimozione 'Errato':")
for g in giocatori_con_totale:
    print(f"  {g['nome']}: Livello {g['livello']}, Punti Totali {g['punti_totali']}")
print("-" * 30)

# ====================================================================
# Task B (parte 2): Filtro
# Scarta i giocatori sotto il Punteggio Minimo.
# ====================================================================

# Usiamo una list comprehension (o filter() con lambda) per il filtraggio
giocatori_qualificati: List[Dict[str, Any]] = [
]

print(f"\n--- 3. Risultato Filtro (Minimo {PUNTEGGIO_MINIMO_QUALIFICAZIONE}) ---")
print("Giocatori Qualificati:")
for g in giocatori_qualificati:
    print(f"  {g['nome']} (Punti: {g['punti_totali']})")
print("-" * 30)

# ====================================================================
# Task C: Ordinamento Complesso
# Ordina per Livello (decrescente) e poi Punti Totali (decrescente).
# ====================================================================

# Uso di 'lambda' e tupla per ordinamento multi-criterio.
# La tupla è: (-livello, -punti_totali) perché vogliamo decrescente per entrambi.
giocatori_ordinati = sorted(
    giocatori_qualificati,
    key=None
)

print("\n--- 4. Risultato Ordinamento Complesso (lambda) ---")
print("Ordinati per Livello (DEC) e Punti Totali (DEC):")
for g in giocatori_ordinati:
    print(f"  {g['nome']}: Livello {g['livello']} | Punti Totali {g['punti_totali']}")
print("-" * 30)

# ====================================================================
# Task D: Riduzione (reduce)
# Calcola il Punteggio Totale medio dei giocatori qualificati.
# ====================================================================

if giocatori_qualificati:
    # 1. Calcolo del totale cumulativo usando reduce
    # acc è l'accumulatore (somma parziale), g è l'elemento corrente (dizionario)
    somma_punti_totali = reduce(
        lambda acc, g: None,
        giocatori_qualificati,
        0  # 0 è il valore iniziale dell'accumulatore
    )

    # 2. Calcolo della media
    media_punti = somma_punti_totali / len(giocatori_qualificati)

    print("\n--- 5. Risultato Riduzione (reduce) ---")
    print(f"Punti Totali Cumulativi (con reduce): {somma_punti_totali}")
    print(f"Numero di giocatori qualificati: {len(giocatori_qualificati)}")
    print(f"Punteggio Medio Giocatori Qualificati: {media_punti:.2f}")
else:
    print("\n--- 5. Risultato Riduzione (reduce) ---")
    print("Nessun giocatore qualificato, media non calcolabile.")