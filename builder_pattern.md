# 🧱 Builder Pattern --- Explication Simple & Exemples en Python

Le **Builder Pattern** permet de construire des objets *complexes* étape
par étape,\
sans exposer la logique interne de construction au code client.

On l'utilise lorsque : - un objet nécessite **beaucoup de
paramètres**, - la création doit être **découpée en étapes**, - il
existe **plusieurs variantes** possibles du même objet.

------------------------------------------------------------------------

# ✅ 1. Principe du Builder Pattern

> *Séparer la construction d'un objet complexe de sa représentation
> finale.*\
> Ainsi, le même processus de construction peut créer différentes
> représentations.

Le Builder est composé de : - **Director** (orchestrateur) ---
*optionnel* - **Builder** (interface) - **Concrete Builders** -
**Product** (objet final)

------------------------------------------------------------------------

# 🟦 2. Exemple simple : création d'un ordinateur (PC Builder)

## Produit final

``` python
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"CPU={self.cpu}, RAM={self.ram}, STORAGE={self.storage}"
```

------------------------------------------------------------------------

## Interface Builder

``` python
class ComputerBuilder:
    def set_cpu(self): pass
    def set_ram(self): pass
    def set_storage(self): pass
    def build(self): pass
```

------------------------------------------------------------------------

## Builder concret

``` python
class GamingPCBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel i9"
        return self

    def set_ram(self):
        self.computer.ram = "32GB"
        return self

    def set_storage(self):
        self.computer.storage = "1TB SSD"
        return self

    def build(self):
        return self.computer
```

------------------------------------------------------------------------

## Director (optionnel)

``` python
class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_gaming_pc(self):
        return (self.builder
                .set_cpu()
                .set_ram()
                .set_storage()
                .build())
```

------------------------------------------------------------------------

## Utilisation

``` python
builder = GamingPCBuilder()
director = Director(builder)

pc = director.construct_gaming_pc()
print(pc)
```

### Output :

    CPU=Intel i9, RAM=32GB, STORAGE=1TB SSD

------------------------------------------------------------------------

# 🟩 3. Variante plus simple (style Fluent Builder)

Très utilisée en Python pour simplifier la création d'objets avec
beaucoup d'options.

``` python
class UserBuilder:
    def __init__(self):
        self.name = None
        self.age = None
        self.email = None

    def with_name(self, name):
        self.name = name
        return self

    def with_age(self, age):
        self.age = age
        return self

    def with_email(self, email):
        self.email = email
        return self

    def build(self):
        return {"name": self.name, "age": self.age, "email": self.email}
```

------------------------------------------------------------------------

## Utilisation

``` python
user = (
    UserBuilder()
    .with_name("Alice")
    .with_age(28)
    .with_email("alice@example.com")
    .build()
)

print(user)
```

### Output :

    {'name': 'Alice', 'age': 28, 'email': 'alice@example.com'}

------------------------------------------------------------------------

# 🟨 4. Schéma visuel

    Director → Builder → (steps) → Product

Ou sans directeur :

    Client → Builder → Product

------------------------------------------------------------------------

# 🟪 5. Explication courte pour entretien

> *Le Builder permet de construire un objet complexe étape par étape.\
> Il sépare la logique de construction de sa représentation finale,\
> et permet de créer différentes variantes d'un même objet en
> réutilisant le même processus.*

------------------------------------------------------------------------

# 🏁 Conclusion

Le **Builder Pattern** est extrêmement utile lorsque : - l'objet final
contient beaucoup de paramètres, - il existe plusieurs configurations
possibles, - la construction doit être fluide, lisible et modulaire.

Python permet une implémentation simple, soit en version "classique",
soit en version "Fluent Builder".
