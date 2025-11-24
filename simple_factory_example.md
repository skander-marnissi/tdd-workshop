# 🏭 Simple Factory Pattern --- Exemple Python

Ce document présente un exemple clair du **Simple Factory Pattern**,
idéal pour les entretiens techniques.

------------------------------------------------------------------------

# 🔹 1. Produits (Shapes)

``` python
class Shape:
    def draw(self):
        raise NotImplementedError
```

``` python
class Circle(Shape):
    def draw(self):
        print("Je dessine un cercle")
```

``` python
class Square(Shape):
    def draw(self):
        print("Je dessine un carré")
```

``` python
class Triangle(Shape):
    def draw(self):
        print("Je dessine un triangle")
```

------------------------------------------------------------------------

# 🔹 2. Simple Factory

``` python
class ShapeFactory:

    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        shape_type = shape_type.lower()

        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError(f"Shape '{shape_type}' not recognized")
```

------------------------------------------------------------------------

# 🔹 3. Utilisation

``` python
shape = ShapeFactory.create_shape("circle")
shape.draw()
```

**Output :**

    Je dessine un cercle

------------------------------------------------------------------------

# 🧠 Résumé pour entretien

-   Le Simple Factory encapsule la logique d'instanciation.\
-   Le client ne connaît pas les classes concrètes.\
-   Évite les if/else partout dans le code.\
-   Très utilisé pour créer des objets simples selon un paramètre.
