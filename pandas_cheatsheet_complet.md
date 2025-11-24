# 📌 Pandas -- Cheat Sheet Complet (Chargement, Filtrage, Transformation, Agrégations, GroupBy, Pivot, Merge)

------------------------------------------------------------------------

# 🟦 1. Charger des fichiers CSV

### Chargement simple

``` python
import pandas as pd
df = pd.read_csv("data.csv")
```

### Avec séparateur

``` python
df = pd.read_csv("data.csv", sep=";")
```

### Sélection de colonnes

``` python
df = pd.read_csv("data.csv", usecols=["id", "name"])
```

### Encodage

``` python
df = pd.read_csv("data.csv", encoding="utf-8")
```

------------------------------------------------------------------------

# 🟩 2. Charger des fichiers Parquet

### Simple

``` python
df = pd.read_parquet("data.parquet")
```

### Avec pyarrow (recommandé)

``` python
df = pd.read_parquet("data.parquet", engine="pyarrow")
```

------------------------------------------------------------------------

# 🟥 3. Visualisation (matplotlib)

``` python
import matplotlib.pyplot as plt
```

### Graphique en ligne

``` python
df.plot(x="date", y="price")
plt.show()
```

### Graphique en barres

``` python
df.groupby("category")["sales"].sum().plot(kind="bar")
plt.show()
```

### Scatter plot

``` python
df.plot.scatter(x="age", y="income")
plt.show()
```

------------------------------------------------------------------------

# 🟨 4. Filtrage

### Condition simple

``` python
df[df["age"] > 30]
```

### Conditions multiples

``` python
df[(df["age"] > 30) & (df["country"] == "FR")]
```

### Avec query()

``` python
df.query("age > 30 and country == 'FR'")
```

### Avec isin()

``` python
df[df["country"].isin(["FR", "DE", "ES"])]
```

### Négation

``` python
df[~df["country"].isin(["FR", "DE"])]
```

### Filtre sur chaînes

``` python
df[df["name"].str.startswith("M")]
df[df["email"].str.contains("@gmail.com")]
```

### Filtre sur valeurs dupliquées

``` python
df[df.duplicated("email", keep=False)]
```

### Filtre sur valeurs nulles

``` python
df[df["col"].isna()]
df[df["col"].notna()]
```

------------------------------------------------------------------------

# 🟧 5. Renommage de colonnes

``` python
df = df.rename(columns={"old_name": "new_name"})
```

------------------------------------------------------------------------

# 🟨 6. Changement de type

### Conversion simple

``` python
df["col"] = df["col"].astype(int)
df["col"] = df["col"].astype(float)
df["col"] = df["col"].astype("string")
```

### Convertir en datetime

``` python
df["date"] = pd.to_datetime(df["date"])
```

### Inférence automatique des types

``` python
df = df.convert_dtypes()
```

------------------------------------------------------------------------

# 🟩 7. Remplir les valeurs manquantes (fillna)

### Avec une valeur

``` python
df["col"] = df["col"].fillna(0)
```

### Avec une autre colonne

``` python
df["col"] = df["col"].fillna(df["autre_col"])
```

------------------------------------------------------------------------

# 🟦 8. Pivot Table

``` python
df.pivot_table(
    index="category",
    columns="year",
    values="sales",
    aggfunc="sum"
)
```

------------------------------------------------------------------------

# 🟧 9. Concaténation de DataFrames

### Concat vertical

``` python
df3 = pd.concat([df1, df2], axis=0)
```

### Concat horizontal

``` python
df3 = pd.concat([df1, df2], axis=1)
```

------------------------------------------------------------------------

# 🟦 10. Melt (dénormalisation)

``` python
df_melt = df.melt(id_vars=["id"], var_name="variable", value_name="valeur")
```

------------------------------------------------------------------------

# 🟥 11. Tri

### Tri simple

``` python
df.sort_values("age")
```

### Tri multiple

``` python
df.sort_values(["age", "income"], ascending=[True, False])
```

------------------------------------------------------------------------

# 🟨 12. Compter les valeurs

### Count simple

``` python
df["city"].count()
```

### Count distinct

``` python
df["city"].nunique()
```

### Tableau croisé de comptage

``` python
df["city"].value_counts()
```

------------------------------------------------------------------------

# 🟦 13. Agrégations --- les plus utilisées

### Fonctions classiques

``` python
df["price"].sum()
df["price"].mean()
df["price"].median()
df["price"].min()
df["price"].max()
df["price"].std()
df["price"].var()
df["price"].nunique()
df["price"].count()
```

### Agrégations multiples

``` python
df.agg({
    "price": ["sum", "mean", "max"],
    "qty": ["min", "max"]
})
```

------------------------------------------------------------------------

# 🟧 14. GroupBy

### Somme par groupe

``` python
df.groupby("category")["sales"].sum()
```

### Agrégations multiples modernes

``` python
df.groupby("category", as_index=False).agg(
    total_sales=("sales", "sum"),
    avg_qty=("quantity", "mean"),
    unique_customers=("customer_id", "nunique")
)
```

### Filtrer après groupby

``` python
df.groupby("region").filter(lambda x: x["sales"].sum() > 10000)
```

------------------------------------------------------------------------

# 🟥 15. Jointures (merge)

### Inner join

``` python
df1.merge(df2, on="id")
```

### Left join

``` python
df1.merge(df2, on="id", how="left")
```

### Right join

``` python
df1.merge(df2, on="id", how="right")
```

### Outer join

``` python
df1.merge(df2, on="id", how="outer")
```

### Jointure sur plusieurs colonnes

``` python
df1.merge(df2, on=["country", "year"])
```

### Colonnes de noms différents

``` python
df1.merge(df2, left_on="user_id", right_on="id")
```

------------------------------------------------------------------------

# 🎤 Résumé oral (entretien)

> Avec Pandas, je charge les données (`read_csv`, `read_parquet`),\
> j'analyse via les filtres (`isin`, conditions, `query`),\
> j'agrège (`groupby`, `agg`, `value_counts`),\
> je transforme (`pivot`, `melt`, `concat`),\
> je nettoie (`drop_duplicates`, `fillna`, changement de type),\
> et je visualise avec `df.plot()`.\
> C'est tout le workflow Data classique.
