# 🔒 Singleton Pattern --- Exemple Python Clair & Professionnel

Ce document présente un **exemple simple, propre et adapté à un
entretien technique** du *Design Pattern Singleton* en Python.

------------------------------------------------------------------------

# ✅ 1. Principe du Singleton

Le **Singleton** garantit qu'une classe :

-   n'a **qu'une seule instance** dans tout le programme,\
-   et que cette instance est **accessible globalement**.

Il est souvent utilisé pour : - gestion de configuration\
- connexion à une base de données\
- logger global\
- cache partagé

------------------------------------------------------------------------

# 🟦 2. Implémentation classique du Singleton

### 🎯 Objectif

Empêcher la création de plusieurs objets, même si le code appelle
plusieurs fois la classe.

------------------------------------------------------------------------

## 🧱 Code du Singleton

``` python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

------------------------------------------------------------------------

## 🧱 Utilisation

``` python
a = Singleton()
b = Singleton()
print(a is b)
```

### 📌 Résultat :

    True

➡️ `a` et `b` pointent exactement vers **la même instance**.

------------------------------------------------------------------------

# 🟩 3. Version élégante : Singleton via décorateur

Python permet une version plus moderne :

``` python
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
```

### Utilisation :

``` python
@singleton
class Database:
    def __init__(self):
        print("Connexion établie")
```

``` python
db1 = Database()
db2 = Database()
print(db1 is db2)
```

### Résultat :

    Connexion établie
    True

(On ne voit "Connexion établie" qu'une seule fois.)

------------------------------------------------------------------------

# 🟧 4. Schéma visuel

    Appel 1 → Singleton → crée instance
    Appel 2 → Singleton → renvoie instance existante
    Appel 3 → Singleton → renvoie instance existante

------------------------------------------------------------------------

# 🟨 5. Ce qu'il faut dire en entretien

> *Un Singleton garantit une seule instance pour toute l'application.\
> En Python, on peut l'implémenter via `__new__` ou via un décorateur.\
> C'est utile pour les ressources globales comme la configuration, les
> logs ou les connexions.\
> Il ne faut pas en abuser car cela introduit un état global difficile à
> tester.*

------------------------------------------------------------------------

# 🟫 6. Cas d'usage professionnels

-   **Logging global** (un seul logger partagé)\
-   **Connexion unique à une base de données**\
-   **Manager centralisé de configuration**\
-   **Cache applicatif**\
-   **Gestionnaire d'événements unique**

------------------------------------------------------------------------

# 🏁 Conclusion

Le Singleton est un pattern simple mais puissant, à utiliser avec
précaution.\
Il garantit une instance unique, et Python permet de l'implémenter très
simplement via `__new__` ou via un décorateur.
