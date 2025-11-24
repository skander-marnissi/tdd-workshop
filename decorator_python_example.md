# 🎨 Décorateur Python --- Exemple Clair et Professionnel

Ce document présente un **exemple propre, simple et utile du pattern
Décorateur en Python**, basé sur la syntaxe `@decorator`.\
Il est parfait pour la préparation d'un entretien technique.

------------------------------------------------------------------------

# ✅ 1. Le principe du Décorateur

Un décorateur en Python permet :

-   d'ajouter du comportement **avant ou après** l'exécution d'une
    fonction,
-   **sans modifier la fonction originale**,
-   en gardant une syntaxe simple grâce à `@mon_decorateur`.

Cela correspond au **Design Pattern Decorator** en POO, mais adapté au
style Python.

------------------------------------------------------------------------

# 🟦 2. Exemple : Décorateur de logging

### 🎯 Objectif

Afficher automatiquement un message à chaque appel de fonction (ex :
audit, debug, monitoring).

------------------------------------------------------------------------

## 🧱 Code du décorateur

``` python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Appel de la fonction : {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

------------------------------------------------------------------------

## 🧱 Utilisation avec @annotation

``` python
@log
def greet(name):
    print(f"Bonjour {name} !")
```

------------------------------------------------------------------------

## 🧱 Appel

``` python
greet("Alice")
```

### 📌 Résultat

    [LOG] Appel de la fonction : greet
    Bonjour Alice !

➡️ La fonction *greet* n'a pas été modifiée, mais enrichie
automatiquement.

------------------------------------------------------------------------

# 🟩 3. Exemple avancé : Décorateur de timing (mesure de performance)

### 🎯 Objectif

Mesurer automatiquement le temps d'exécution d'une fonction (utile en
Data, API, ML).

------------------------------------------------------------------------

## 🧱 Code du décorateur

``` python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} exécutée en {end - start:.4f} s")
        return result
    return wrapper
```

------------------------------------------------------------------------

## 🧱 Utilisation

``` python
@timer
def slow_task():
    time.sleep(1)
    print("Tâche terminée")
```

------------------------------------------------------------------------

## 🧱 Appel

``` python
slow_task()
```

### 📌 Résultat

    Tâche terminée
    [TIMER] slow_task exécutée en 1.0001 s

------------------------------------------------------------------------

# 🟨 4. Comment expliquer cela en entretien

> Un décorateur est une fonction qui prend une autre fonction en
> paramètre et renvoie une version enrichie de cette fonction.\
> La syntaxe @decorator applique automatiquement cette transformation.\
> Cela permet d'ajouter des fonctionnalités transverses (logging,
> sécurité, timing, cache) sans toucher au code métier.

------------------------------------------------------------------------

# 🟪 5. Schéma simplifié

    greet() 
       ↓ décoré par
    @log
       ↓ devient
    wrapper() → log → greet()

------------------------------------------------------------------------

# 🟧 6. Cas d'usage professionnels courants

-   Logging / audit automatique\
-   Cache (ex : `functools.lru_cache`)\
-   Vérification d'authentification (FastAPI)\
-   Retry automatique\
-   Validation d'inputs\
-   Time profiling de fonctions lourdes

------------------------------------------------------------------------

# 🏁 Conclusion

Le décorateur est l'un des outils les plus puissants et élégants de
Python.\
Il permet d'ajouter des responsabilités à une fonction ou méthode **sans
duplication**, **sans modifier le code source**, et **de manière
réutilisable**.
