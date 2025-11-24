# 🌳 Pattern Composite --- Explication Simple & Exemples en Python

Le **pattern Composite** permet de gérer **des structures
hiérarchiques** (comme des arbres) où : - certains objets sont
**simples** (feuilles), - d'autres sont **des conteneurs** qui
regroupent d'autres objets (composites), - mais tous partagent **la même
interface**.

Cela permet au code client de manipuler chaque élément **exactement de
la même manière**, qu'il soit simple ou composé.

------------------------------------------------------------------------

# 🧩 1. Principe du Pattern Composite

> **Traiter de manière uniforme des objets simples et des objets
> composés.**

Le pattern Composite rend possible :

-   d'appeler la même méthode sur un élément simple ou un composite,
-   de construire des structures d'objets imbriquées,
-   de naviguer et d'exécuter des actions récursivement.

C'est parfait pour représenter : - fichiers & dossiers\
- menus et sous-menus\
- expressions mathématiques\
- structures arborescentes

------------------------------------------------------------------------

# 🌱 2. Exemple simple : Fichiers & Dossiers

## 🔹 Interface commune

``` python
class FileSystemItem:
    def show(self):
        raise NotImplementedError
```

------------------------------------------------------------------------

## 🔹 Feuille : un fichier

``` python
class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"📄 Fichier : {self.name}")
```

------------------------------------------------------------------------

## 🔹 Composite : un dossier contenant d'autres éléments

``` python
class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def show(self):
        print(f"📁 Dossier : {self.name}")
        for child in self.children:
            child.show()
```

------------------------------------------------------------------------

## 🔹 Utilisation

``` python
root = Folder("Racine")
root.add(File("notes.txt"))
root.add(File("todo.txt"))

sub = Folder("Images")
sub.add(File("chat.png"))
sub.add(File("chien.jpg"))

root.add(sub)

root.show()
```

### ⭐ Output

    📁 Dossier : Racine
    📄 Fichier : notes.txt
    📄 Fichier : todo.txt
    📁 Dossier : Images
    📄 Fichier : chat.png
    📄 Fichier : chien.jpg

------------------------------------------------------------------------

# 🔢 3. Exemple 2 : Expressions mathématiques

## Interface commune

``` python
class Expression:
    def evaluate(self):
        raise NotImplementedError
```

------------------------------------------------------------------------

## Feuille : nombre

``` python
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value
```

------------------------------------------------------------------------

## Composite : addition

``` python
class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
```

------------------------------------------------------------------------

## Utilisation

``` python
expr = Add(Number(5), Add(Number(3), Number(2)))
print(expr.evaluate())
```

Output :

    10

------------------------------------------------------------------------

# 🧠 4. Résumé à dire en entretien

> *Composite permet de représenter des objets en arborescence.\
> Il unifie le traitement des objets simples (feuilles) et des objets
> composés\
> grâce à une interface commune.\
> Le code client ne fait aucune distinction : il peut appeler la même
> méthode\
> sur un fichier, un dossier, une expression mathématique, etc.*

------------------------------------------------------------------------

# 🏁 Conclusion

Le **Composite Pattern** est essentiel dès qu'il faut manipuler des
structures hiérarchiques.\
C'est l'un des patterns les plus élégants car il combine : -
simplicité, - réutilisabilité, - extensibilité, - récursivité naturelle.
