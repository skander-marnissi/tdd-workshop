# 🏭 Design Pattern --- Factory Method (Exemples en Python)

Ce document contient **tous les exemples du pattern Factory Method**
expliqués précédemment, dans une version compacte et prête à relire
avant un entretien.

------------------------------------------------------------------------

# 🎯 1. Interface du Produit

``` python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
```

------------------------------------------------------------------------

# 🎯 2. Produits Concrets

``` python
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Envoi Email : {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Envoi SMS : {message}")

class PushNotification(Notification):
    def send(self, message: str):
        print(f"Envoi Push : {message}")
```

------------------------------------------------------------------------

# 🎯 3. Factory Method (Classe abstraite)

``` python
class NotificationCreator(ABC):

    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def send_notification(self, message: str):
        notification = self.create_notification()
        notification.send(message)
```

------------------------------------------------------------------------

# 🎯 4. Factories Concrètes

``` python
class EmailCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()

class PushCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return PushNotification()
```

------------------------------------------------------------------------

# 🎯 5. Utilisation

``` python
creator = SMSCreator()
creator.send_notification("Votre code est 1234.")
```

**Output :**

    Envoi SMS : Votre code est 1234.

------------------------------------------------------------------------

# 🧠 Résumé Court (pour entretien)

-   Factory Method délègue la création d'objets aux sous-classes.
-   Le code client ne connaît pas les classes concrètes.
-   Ajout de nouveaux types = pas besoin de modifier le code existant.
-   Respect du principe **Open/Closed (OCP)**.
