"""
Crée ``data/raw/fake_social_media_messy.csv`` à partir du CSV Kaggle.

Les défauts sont introduits de façon **reproductible** (graine fixe) pour pouvoir
exercer nettoyage / EDA dans le notebook sans modifier l’original.

À lancer depuis la racine du dépôt :

    python scripts/make_messy_dataset.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "fake_social_media.csv"
DST = ROOT / "data" / "raw" / "fake_social_media_messy.csv"


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Fichier source introuvable : {SRC}")

    rng = np.random.default_rng(42)
    df = pd.read_csv(SRC)

    dup = df.sample(n=35, replace=True, random_state=42)
    messy = pd.concat([df, dup], ignore_index=True)

    num_cols = messy.select_dtypes(include=[np.number]).columns.tolist()
    num_cols.remove("is_fake")

    n_cells = messy.shape[0] * len(num_cols)
    n_nan = max(1, int(n_cells * 0.04))
    flat = rng.choice(n_cells, size=n_nan, replace=False)
    rows = flat // len(num_cols)
    cols_i = flat % len(num_cols)

    for ri, ci in zip(rows, cols_i):
        cname = num_cols[ci]
        messy.iloc[ri, messy.columns.get_loc(cname)] = np.nan

    idx_plat = rng.choice(messy.index, size=max(1, int(len(messy) * 0.14)), replace=False)
    repl = {"Instagram": "instagram", "Facebook": "FACEBOOK", "Twitter": "TwItTeR"}
    messy.loc[idx_plat, "platform"] = messy.loc[idx_plat, "platform"].astype(str).replace(repl)

    out_idx = rng.choice(messy.index, size=12, replace=False)
    messy.loc[out_idx, "followers"] = messy.loc[out_idx, "followers"].clip(lower=1) * 5000

    messy.to_csv(DST, index=False)
    print(f"Écrit : {DST}")
    print(f"Lignes : {messy.shape[0]} (dont {len(dup)} doublons ajoutés)")
    print(f"Valeurs NaN : {messy.isna().sum().sum()}")
    print("Indiquez dans le rapport que ces anomalies sont volontaires (script documenté).")


if __name__ == "__main__":
    main()
