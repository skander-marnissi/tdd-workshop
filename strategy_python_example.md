# ♟️ Strategy Pattern --- Exemple Python Clair & Professionnel

Ce document présente un **exemple simple, propre et parfaitement adapté
à un entretien technique** du *Design Pattern Strategy* en Python.

------------------------------------------------------------------------

# ✅ 1. Principe du Strategy Pattern

Le **Strategy Pattern** permet de :

-   changer **dynamiquement** l'algorithme utilisé,
-   séparer l'algorithme du code métier,
-   respecter le principe **Open/Closed** (ajouter des stratégies sans
    modifier le client).

C'est extrêmement utile pour : - pricing\
- rules engine\
- sélection algorithmique\
- moteurs de calcul\
- data processing

------------------------------------------------------------------------

# 🟦 2. Exemple concret : différents algorithmes de tri

### 🎯 Scénario

Votre application veut trier une liste,\
mais selon le contexte, vous souhaitez changer l'algorithme :

-   Bubble Sort\
-   Quick Sort\
-   Merge Sort

➡️ Le client ne doit pas connaître l'algorithme exact.

------------------------------------------------------------------------

# 🧱 3. Interface des stratégies

``` python
class SortStrategy:
    def sort(self, data):
        raise NotImplementedError
```

------------------------------------------------------------------------

# 🟩 4. Stratégies concrètes

``` python
class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Tri avec BubbleSort")
        return sorted(data)  # simplification
```

``` python
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Tri avec QuickSort")
        return sorted(data)
```

``` python
class MergeSort(SortStrategy):
    def sort(self, data):
        print("Tri avec MergeSort")
        return sorted(data)
```

------------------------------------------------------------------------

# 🟧 5. Le Contexte (utilise la stratégie choisie)

``` python
class SortingContext:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy.sort(data)
```

------------------------------------------------------------------------

# 🟨 6. Utilisation

``` python
context = SortingContext(BubbleSort())
context.execute([5, 3, 8])

context.set_strategy(QuickSort())
context.execute([5, 3, 8])
```

### 📌 Résultat :

    Tri avec BubbleSort
    Tri avec QuickSort

------------------------------------------------------------------------

# 🟪 7. Schéma visuel

    Client → Context → (Strategy.sort)
                       ↑
     BubbleSort / QuickSort / MergeSort

------------------------------------------------------------------------

# 🟫 8. Ce qu'il faut dire en entretien

> *Strategy isole les algorithmes derrière une interface commune.\
> Le contexte peut alors changer la stratégie dynamiquement,\
> et on peut ajouter de nouvelles stratégies sans modifier le code
> client.*

------------------------------------------------------------------------

# 🏁 Conclusion

Le **Strategy Pattern** est un des plus importants en Python et en
ingénierie logicielle :\
il permet de changer de comportement sans réécrire ou toucher au reste
de l'application.
