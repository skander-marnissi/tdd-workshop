# FICHE D'ENTRETIEN --- VERSION SENIOR (Optimisée & Réorganisée)

## 🔥. Script d'ouverture

> "Pour bien comprendre votre contexte, je vais vous poser des questions
> sur votre architecture, votre stack technique, vos contraintes de
> production, vos workflows d'équipe et vos objectifs. L'objectif est de
> comprendre où je peux vous apporter de la valeur."


------------------------------------------------------------------------

## 🔵 1. FastAPI (API design, sécurité, performance)

### Architecture & Structure

-   Comment structurez-vous vos endpoints ? *(routers, modules,
    startup/shutdown --- structure du projet)*
-   Utilisez-vous des modèles Pydantic v2 ? *(validation/sérialisation
    moderne)*
-   Comment gérez-vous la validation & sérialisation ? *(middleware,
    DTO, pydantic-core)*

### Performance

-   Quel serveur ASGI utilisez-vous ? *(Uvicorn/Gunicorn --- scaling
    CPU)*
-   Avez-vous du caching ? *(Redis, backends FastAPI)*
-   Utilisez-vous du rate limiting ? *(protection API)*

### Sécurité

-   Comment gérez-vous l'authentification ? *(JWT, OAuth2, API keys,
    providers)*
-   Quels middlewares de sécurité utilisez-vous ? *(CORS, headers, HTTPS
    redirect)*
-   Comment gérez-vous les rôles/permissions ? *(RBAC, ABAC, scopes)*

### Qualité / Tests

-   Utilisez-vous TestClient pour les tests d'intégration ? *(tests API
    réels)*
-   Avez-vous des tests dédiés aux schémas Pydantic ? *(contrats de
    données)*

### Logs & Observabilité

-   Comment logguez-vous les requêtes ? *(structured logs, JSON,
    correlation ID)*
-   Avez-vous du tracing distribué ? *(OpenTelemetry)*

------------------------------------------------------------------------

## 🟢 2. MongoDB (modélisation, migrations, scalabilité)

### Architecture & Modélisation

-   Cluster shardé ou replica set ? *(HA, scaling lecture/écriture)*
-   Comment structurez-vous vos collections ? *(domaine, feature,
    microservice)*
-   Quel niveau de normalisation utilisez-vous ? *(embed vs reference)*
-   Comment gérez-vous les documents volumineux ? *(limite 16MB)*

### Performance

-   Comment gérez-vous les workloads intensifs ? *(pipelines agg,
    indexing, TTL)*

### Migrations MongoDB

-   Quel outil utilisez-vous pour gérer les migrations ? *(Mongock,
    Mongo-Migrate...)*
-   Les migrations sont-elles versionnées ? *(tracking & audit)*
-   Comment déployez-vous les migrations en production ? *(rolling,
    zero-downtime)*
-   Existe-t-il un mécanisme de rollback ? *(sécurité data)*

------------------------------------------------------------------------

## 🟡 3. Pandas / Data Engineering

### Performance

-   Quels volumes de données traitez-vous ? *(taille dataset → outils)*
-   Quelles optimisations Pandas utilisez-vous ? *(chunking, dtypes,
    vectorisation)*

### Qualité / Validation

-   Comment validez-vous les datasets ? *(Pandera, Pydantic, Great
    Expectations)*
-   Avez-vous des pipelines standardisés de nettoyage ? *(ETL interne)*
-   Disposez-vous d'un schéma standardisé pour les datasets ? *(contrat
    de données)*

### DataOps

-   Quelles règles qualité appliquez-vous ? *(nulls, ranges, doublons)*
-   Utilisez-vous des tests automatiques sur les DataFrames ? *(pipeline
    qualité)*
-   Comment versionnez-vous les datasets ? *(DVC, MLflow, DeltaLake)*
-   Prefect pour créer une pipeline et faire du monitoring des process des batch avec deltatable et mongodb 

------------------------------------------------------------------------

## 🟣 4. Gouvernance & Process

-   Quelles conventions de naming utilisez-vous ? *(cohérence across
    repos)*
-   Avez-vous des outils de mise à jour automatique ? *(Dependabot,
    Renovate)*

------------------------------------------------------------------------

## 🔐 5. Sécurité & Secrets

-   Comment gérez-vous les secrets ? *(Vault, KMS, Secret Manager,
    SealedSecrets)*
-   Avez-vous une rotation automatique des secrets ? *(compliance /
    sécurité)*

------------------------------------------------------------------------

## 🟤 6. Git / Repo Management

-   Utilisez-vous les conventional commits ? *(qualité des PR /
    changelog)*
-   Utilisez-vous des git hooks ? *(pre-commit pour lint/tests)*
-   Utilisez-vous les GitHub/GitLab Secrets ? *(sécurité pipelines)*
-   Comment organisez-vous vos repos ? *(monorepo, multi-repo,
    séparation API/batch/chart)*

------------------------------------------------------------------------

## 🔧 7. CI/CD & Déploiement

-   Quel outil CI/CD utilisez-vous ? *(GitHub Actions, GitLab CI,
    Jenkins)*
-   Votre pipeline est-il GitOps ou classique ? *(ArgoCD/Flux vs CI
    deploy)*
-   Comment versionnez-vous les images Docker ? *(SHA, SemVer)*
-   Comment gérez-vous les rollback ? *(Helm rollback, stratégie de
    release)*
-   Quels environnements utilisez-vous ? *(dev, staging, preprod, prod)*
-   Faites-vous du scanning de vulnérabilités ? *(Trivy, Harbor, ECR
    scan)*

------------------------------------------------------------------------

## 🟦 8. Kubernetes

### Architecture Cluster

-   Quel Ingress Controller utilisez-vous ? *(NGINX, Traefik, Istio)*
-   Comment gérez-vous les secrets Kubernetes ? *(Vault, SealedSecrets)*
-   Comment est structuré votre cluster ? *(node pools, séparation env)*
-   Mono-cluster ou multi-cluster ? *(isolation forte)*
-   Niveau d'isolation ? *(namespace par équipe/projet)*

### Scalabilité

-   Comment gérez-vous l'autoscaling ? *(HPA, VPA, autoscaler)*

### Qualité / Déploiement

-   Avez-vous des tests d'intégration sous K8s ? *(vraie validation)*
-   Comment validez-vous un déploiement ? *(canary, blue/green,
    progressive delivery)*
-   Utilisez-vous des environnements éphémères ? *(preview env)*

------------------------------------------------------------------------

## 🟫 9. Observabilité (logs, metrics, tracing)

-   Quelle stack de monitoring utilisez-vous ? *(Prometheus, Grafana,
    Datadog...)*
-   Avez-vous des dashboards SLO/SLI ? *(maturité SRE)*
-   Avez-vous un système d'alerting ? *(PagerDuty, Opsgenie)*
-   Faites-vous du tracing distribué ? *(OpenTelemetry, Jaeger)*
-   Comment corrélez-vous les requêtes ? *(correlation-ID)*

------------------------------------------------------------------------

## 🟩 10. Python (pratiques, packaging, workflow)

-   Quel package manager utilisez-vous ? *(Poetry, PDM, uv)*
-   Quel cycle de développement suivez-vous ? *(spec-first, TDD,
    code-first)*
-   Comment gérez-vous les migrations DB ? *(Alembic vs NoSQL
    migrations)*

------------------------------------------------------------------------

## 🧪 11. Testing (unitaires, intégration, e2e)

-   Niveau de couverture test ? *(maturité QA)*
-   Séparation claire U/I/E2E ? *(architecture tests)*
-   Utilisez-vous des fixtures globales ? *(Pytest config)*
-   Avez-vous une base de test dockerisée ? *(tests réalistes)*
-   Tests exécutés automatiquement en CI ? *(pipeline qualité)*

------------------------------------------------------------------------

## 🧱 12. Clean Architecture / Refactoring

-   Quelle architecture utilisez-vous ? *(Clean, Hexagonal, DDD)*
-   Comment gérez-vous les dépendances ? *(inversion des dépendances)*
-   Séparation domain / infrastructure ? *(maintenabilité)*
-   Faites-vous du refactoring régulier ? *(gestion dette technique)*

------------------------------------------------------------------------

## 🎨 13. Design Patterns

-   Quels patterns utilisez-vous le plus ? *(cohérence architecture)*
-   Patterns imposés pour services/repositories ? *(standardisation)*
-   Utilisez-vous des patterns de résilience ? *(Circuit Breaker, Retry,
    Backoff)*

------------------------------------------------------------------------
