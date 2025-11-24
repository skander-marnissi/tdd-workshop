# 👀 Observer Pattern --- Explication Simple & Exemples en Python

Le **pattern Observer** permet de créer un système où : - un objet
principal (**Subject**) *notifie automatiquement* - plusieurs objets
abonnés (**Observers**) - dès qu'un changement se produit.

C'est un pattern parfait pour : - systèmes d'événements, -
notifications, - interfaces graphiques, - monitoring, - architectures
réactives.

------------------------------------------------------------------------

# ✅ 1. Principe du Pattern Observer

> **Un sujet maintient une liste d'observateurs.\
> Lorsqu'un événement se produit, il les notifie tous.**

L'avantage : - le *Subject* n'a **aucune connaissance spécifique** des
observers - les observers peuvent s'abonner / se désabonner librement

------------------------------------------------------------------------

# 🟦 2. Exemple simple : système de notifications

## 🔹 Interface Observer

``` python
class Observer:
    def update(self, message):
        raise NotImplementedError
```

------------------------------------------------------------------------

## 🔹 Sujet (Subject)

``` python
class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
```

------------------------------------------------------------------------

# 🟩 3. Observers concrets

``` python
class EmailNotifier(Observer):
    def update(self, message):
        print(f"[EMAIL] Notification reçue : {message}")
```

``` python
class SMSNotifier(Observer):
    def update(self, message):
        print(f"[SMS] Notification reçue : {message}")
```

------------------------------------------------------------------------

# 🟧 4. Utilisation

``` python
subject = Subject()

email = EmailNotifier()
sms = SMSNotifier()

subject.subscribe(email)
subject.subscribe(sms)

subject.notify("Nouvelle alerte système !")
```

### ⭐ Output :

    [EMAIL] Notification reçue : Nouvelle alerte système !
    [SMS] Notification reçue : Nouvelle alerte système !

------------------------------------------------------------------------

# 🟨 5. Schéma visuel

             ┌──────────────┐
             │    Subject    │
             └───────┬──────┘
                     │ notify()
          ┌──────────┼──────────┐
          ▼          ▼          ▼
    Observer1   Observer2   Observer3
     update()    update()    update()

------------------------------------------------------------------------

# 🟪 6. Exemple supplémentaire : valeur observée

### Sujet

``` python
class TemperatureSensor:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def add(self, obs):
        self.observers.append(obs)

    def set_temperature(self, value):
        self.temperature = value
        self.notify()

    def notify(self):
        for obs in self.observers:
            obs.update(self.temperature)
```

### Observer

``` python
class Display:
    def update(self, value):
        print(f"Nouvelle température : {value}°C")
```

------------------------------------------------------------------------

# 🧠 7. Explication courte à dire en entretien

> *Observer permet d'implémenter un système événementiel où plusieurs
> objets réagissent automatiquement aux changements d'un sujet.\
> Le sujet ne connaît pas les détails des observateurs, ce qui réduit le
> couplage et facilite l'extension.*

------------------------------------------------------------------------

# 🏁 Conclusion

Le **Observer Pattern** est fondamental pour : - les architectures
réactives, - le monitoring, - les bus d'événements, - UI / UX, - les
systèmes temps réel.

Python permet une implémentation simple et élégante en POO.
