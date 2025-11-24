# 🔌 Adapter Pattern --- Exemple Python Clair & Professionnel

Ce document présente un **exemple simple, propre et parfaitement adapté
à un entretien technique** du *Design Pattern Adapter* en Python.

------------------------------------------------------------------------

# ✅ 1. Le principe du Pattern Adapter

L'Adapter permet de :

-   faire communiquer deux interfaces incompatibles,
-   **sans modifier le code existant**,
-   en enveloppant une classe pour qu'elle s'adapte à ce que le client
    attend.

C'est un pattern idéal pour : - intégrer une API externe, - migrer une
ancienne librairie vers une nouvelle, - harmoniser des interfaces
différentes.

------------------------------------------------------------------------

# 🟦 2. Exemple concret : système de paiement

### 🎯 Scénario

Votre application attend une interface simple :

``` python
class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError
```

Mais votre fournisseur de paiement (Stripe, PayPal, autre API) utilise
**une méthode différente**.

➡️ On va utiliser un Adapter pour les faire correspondre.

------------------------------------------------------------------------

# 🧱 3. Classe existante incompatible (API externe)

``` python
class StripeAPI:
    def make_payment(self, amount):
        print(f"Paiement Stripe effectué : {amount}€")
```

➡️ Le problème : il n'y a **pas de méthode pay()**.

------------------------------------------------------------------------

# 🟩 4. L'Adapter --- transforme l'interface

``` python
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe: StripeAPI):
        self.stripe = stripe

    def pay(self, amount):
        self.stripe.make_payment(amount)
```

➡️ Le code client appelle toujours **pay()**,\
➡️ mais la logique réelle est déléguée à **make_payment()**.

------------------------------------------------------------------------

# 🟧 5. Utilisation

``` python
payment = StripeAdapter(StripeAPI())
payment.pay(50)
```

### 📌 Résultat :

    Paiement Stripe effectué : 50€

------------------------------------------------------------------------

# 🟨 6. Schéma visuel

    Client → PaymentProcessor(pay)
               ↑
          StripeAdapter (convertit l'appel)
               ↑
            StripeAPI(make_payment)

------------------------------------------------------------------------

# 🟪 7. Explication courte pour entretien

> *L'Adapter encapsule une classe existante pour lui donner une nouvelle
> interface.\
> Cela permet d'intégrer des systèmes qui n'étaient pas conçus pour
> fonctionner ensemble,\
> sans modifier le code source d'origine.*

------------------------------------------------------------------------

# 🟫 8. Cas d'usage réels

-   Adapter une API externe (Stripe, PayPal, AWS...)\
-   Convertir une librairie obsolète vers une nouvelle interface\
-   Uniformiser plusieurs implémentations différentes\
-   Permettre des tests unitaires en remplaçant l'adapté par un mock\
-   Intégrer plusieurs formats d'entrée (CSV, JSON, XML...)

------------------------------------------------------------------------

# 🏁 Conclusion

Le **Design Pattern Adapter** est essentiel pour la compatibilité et la
migration de systèmes.\
En Python, il est simple à implémenter et extrêmement utile dans les
architectures professionnelles modernes.
