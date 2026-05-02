"""Chargement des fichiers tabulaires depuis ``data/raw``."""

from pathlib import Path

import pandas as pd

from src.paths import DATA_RAW


def load_csv(filename: str | Path, **read_csv_kwargs) -> pd.DataFrame:
    """
    Charge un CSV depuis ``data/raw`` (nom de fichier relatif) ou un chemin absolu.

    Parameters
    ----------
    filename : str | Path
        Ex. ``"profiles.csv"`` ou chemin complet vers un CSV.
    """
    path = Path(filename)
    if not path.is_absolute():
        path = DATA_RAW / path
    if not path.exists():
        raise FileNotFoundError(
            f"Fichier introuvable : {path}. Placez vos données open data dans data/raw/."
        )
    return pd.read_csv(path, **read_csv_kwargs)
