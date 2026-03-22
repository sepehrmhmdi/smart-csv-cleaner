import pandas as pd
import argparse


def clean_csv(
    input_file,
    output_file,
    dedup_column=None,
    drop_missing_columns=None,
    lowercase=False,
    normalize_dates=False,
):
    df = pd.read_csv(input_file)

    initial_rows = len(df)
    stats = {
        "removed_empty": 0,
        "removed_duplicates": 0,
        "removed_missing": 0,
    }

    # 1. Supprimer lignes complètement vides
    before = len(df)
    df = df.dropna(how="all")
    stats["removed_empty"] += before - len(df)

    # 2. Vérifier colonnes demandées
    if dedup_column and dedup_column not in df.columns:
        raise ValueError(f"Colonne '{dedup_column}' introuvable dans le CSV")

    if drop_missing_columns:
        missing_cols = [col for col in drop_missing_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(
                f"Colonnes introuvables pour --drop-missing : {', '.join(missing_cols)}"
            )

    # 3. Nettoyer les colonnes texte
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

        if lowercase:
            df[col] = df[col].str.lower()

    # 4. Convertir chaînes vides en NA
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # 5. Supprimer lignes vides après nettoyage
    before = len(df)
    df = df.dropna(how="all")
    stats["removed_empty"] += before - len(df)

    # 6. Supprimer lignes avec valeurs manquantes spécifiques
    if drop_missing_columns:
        before = len(df)
        df = df.dropna(subset=drop_missing_columns)
        stats["removed_missing"] = before - len(df)

    # 7. Supprimer doublons
    before = len(df)
    if dedup_column:
        df = df.drop_duplicates(subset=[dedup_column])
    else:
        df = df.drop_duplicates()
    stats["removed_duplicates"] = before - len(df)

    # 8. Normalisation des dates
    if normalize_dates:
        for col in df.columns:
            if "date" in col.lower():
                parsed = pd.to_datetime(df[col], errors="coerce", dayfirst=True)
                df[col] = parsed.dt.strftime("%Y-%m-%d")

    final_rows = len(df)

    # 9. Export
    df.to_csv(output_file, index=False)

    # 10. Rapport
    print("\nRAPPORT DE NETTOYAGE")
    print("-" * 30)
    print(f"✔ Lignes initiales        : {initial_rows}")
    print(f"✔ Lignes finales          : {final_rows}")
    print(f"✔ Lignes supprimées       : {initial_rows - final_rows}")
    print(f"  ↳ vides supprimées      : {stats['removed_empty']}")
    print(f"  ↳ doublons supprimés    : {stats['removed_duplicates']}")
    print(f"  ↳ valeurs manquantes    : {stats['removed_missing']}")
    print(f"\nFichier sauvegardé : {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Outil intelligent de nettoyage de CSV"
    )

    parser.add_argument("input", help="Fichier CSV d'entrée")
    parser.add_argument("output", help="Fichier CSV de sortie")

    parser.add_argument(
        "--dedup",
        help="Nom de la colonne pour supprimer les doublons (ex: email)",
    )

    parser.add_argument(
        "--drop-missing",
        nargs="+",
        help="Colonnes obligatoires (supprime lignes si valeur manquante)",
    )

    parser.add_argument(
        "--lowercase",
        action="store_true",
        help="Mettre les colonnes texte en minuscules",
    )

    parser.add_argument(
        "--normalize-dates",
        action="store_true",
        help="Normaliser automatiquement les colonnes contenant 'date'",
    )

    args = parser.parse_args()

    clean_csv(
        args.input,
        args.output,
        dedup_column=args.dedup,
        drop_missing_columns=args.drop_missing,
        lowercase=args.lowercase,
        normalize_dates=args.normalize_dates,
    )