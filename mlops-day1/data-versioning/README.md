# Data Versioning

---

````markdown
# I – MLOps Foundations 
**Prerequisites:** Git, Docker, Miniconda/Anaconda installed on your machine
 > - <a href="https://git-scm.com/about"> About Git </a>
 > - <a href="https://docs.docker.com/"> About Docker </a> 
 > - <a href="https://www.anaconda.com/docs/getting-started/miniconda/main"> About Miniconda/Anaconda </a>  

Ce TP vous fera découvrir les **fondations MLOps** : gestion de code, gestion d’environnement, versioning de données avec DVC.

---

## 🔹 Instructions initiales

1. **Fork** ce repository sur votre compte GitHub.
2. **Clone** le repository localement :
   ```bash
   git clone <url-du-repo>
````

3. **Changer de répertoire** :

   ```bash
   cd Mlops_training
   ```

4. **Créer un environnement Conda** :

   ```bash
   conda env create -f conda.yml
   ```

5. **Activer l’environnement** :

   ```bash
   conda activate mlops_env
   ```

---

## I-2 – Versioning du code

Avant de versionner les données, assurez-vous que **Git fonctionne** et que le code est suivi.

```bash
git status
git add .
git commit -m "Initial commit: base project structure"
```

---

## I-2 – Concepts : Versioning des données avec DVC

**Data Version Control (DVC)** permet de :

* Capturer les versions de vos **données et modèles** dans des commits Git
* Stocker les données **localement ou sur un cloud**
* Basculez facilement entre différentes versions de données

💡 Utilisations typiques : snapshots de données, restauration de versions précédentes, reproductibilité d’expériences, suivi des métriques évolutives.

[En savoir plus sur DVC et le versioning](https://dvc.org/doc/use-cases/versioning-data-and-models)

---

## 🔹 Étape 1 – Initialiser DVC

```bash
dvc init
git commit -m "Initialize DVC"
```

### ⚙️ Configurer l’auto-staging

```bash
dvc config core.autostage true
```

---

## 🔹 Étape 2 – Suivi d’une donnée

1. Suivre le fichier :

```bash
dvc add datastores/raw_data/journal.txt
git commit -m "Track original data datastores/raw_data/journal.txt"
```

2. Ajouter un **tag** pour cette version initiale :

```bash
git tag v0.0 -m "Track original journal.txt"
```

---

## 🔹 Étape 3 – Modifier la donnée

* Ouvrez `datastores/raw_data/journal.txt`
* Ajoutez ou supprimez quelques lignes
* Sauvegardez le fichier

---

## 🔹 Étape 4 – Vérifier le statut des données

```bash
dvc status
```

* Cela montre si des fichiers suivis ont été modifiés.

---

## 🔹 Étape 5 – Versionner la modification

```bash
dvc add datastores/raw_data/journal.txt
git commit -m "Track change of file datastores/raw_data/journal.txt"
git tag -a v0.1 -m "Track change in journal.txt"
```

---

## 🔹 Étape 6 – Naviguer entre les versions de données

```bash
git checkout v0.0
dvc checkout
```

* Vérifiez le fichier `datastores/raw_data/journal.txt`
* Vous revenez à la version initiale du journal.

Pour revenir à la dernière version :

```bash
git checkout main
dvc checkout
```

---

## 🔹 Étape 7 – Ajouter un remote local et partager les données

1. Créer un dossier de stockage :

```bash
mkdir ../dvc_storage
```

2. Ajouter le remote :

```bash
dvc remote add -d localremote ../dvc_storage
git add .dvc/config
git commit -m "Add remote storage"
```

3. Pousser les données vers le remote :

```bash
dvc push
```

4. Supprimer localement le fichier pour tester la restauration :

```bash
rm -rf datastores/raw_data/journal.txt
```

5. Récupérer la donnée depuis le remote :

```bash
dvc pull
```

* Vérifiez que le fichier `journal.txt` est restauré correctement.

---

##  Concept

| Concept               | Commande clé                          | Rôle pédagogique                              |
| --------------------- | ------------------------------------- | --------------------------------------------- |
| Versionner une donnée | `dvc add`                             | DVC suit les fichiers lourds sans polluer Git |
| Commit Git            | `git commit`                          | Versionne la référence aux données            |
| Tag                   | `git tag`                             | Marque un snapshot précis                     |
| Switch version        | `git checkout <tag>` + `dvc checkout` | Revenir à une version antérieure              |
| Remote                | `dvc remote add` + `dvc push`         | Partager les données avec l’équipe            |

---

**Objectifs atteints par ce TP :**

* Découverte du **versioning de données**
* Compréhension de la **relation Git ↔ DVC**
* Premiers exercices de **reproductibilité et collaboration sur les datasets**

---

```

---
