"""Typed geography objects for the Haiti Nippes GIS project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class Commune:
    """Administrative commune within an arrondissement."""

    name: str
    arrondissement: str
    department: str = "Nippes"
    country: str = "Haiti"
    aliases: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Arrondissement:
    """Administrative arrondissement grouping communes."""

    name: str
    communes: tuple[Commune, ...]
    department: str = "Nippes"
    country: str = "Haiti"

    def commune_names(self) -> tuple[str, ...]:
        """Return commune names in stable order."""
        return tuple(commune.name for commune in self.communes)


@dataclass(frozen=True)
class Department:
    """Department-level geography container."""

    name: str
    capital: str
    arrondissements: tuple[Arrondissement, ...]
    country: str = "Haiti"

    def communes(self) -> tuple[Commune, ...]:
        """Flatten all communes into a single tuple."""
        return tuple(
            commune
            for arrondissement in self.arrondissements
            for commune in arrondissement.communes
        )

    def find_commune(self, name: str) -> Commune | None:
        """Find a commune by canonical name or alias."""
        normalized = normalize_name(name)
        for commune in self.communes():
            candidates = (commune.name, *commune.aliases)
            if any(normalize_name(candidate) == normalized for candidate in candidates):
                return commune
        return None


def normalize_name(value: str) -> str:
    """Normalize a geography name for lookup matching."""
    return " ".join(value.casefold().replace("-", " ").split())


def build_nippes_department() -> Department:
    """Build the working Nippes geography model.

    Commune membership should be verified against the selected administrative-boundary
    source before publication outputs are generated.
    """
    miragoane = Arrondissement(
        name="Miragoane",
        communes=(
            Commune(name="Miragoane", arrondissement="Miragoane", aliases=("Miragoane",)),
            Commune(name="Fonds-des-Negres", arrondissement="Miragoane"),
            Commune(name="Paillant", arrondissement="Miragoane"),
            Commune(name="Petite-Riviere-de-Nippes", arrondissement="Miragoane"),
        ),
    )
    anse_a_veau = Arrondissement(
        name="Anse-a-Veau",
        communes=(
            Commune(name="Anse-a-Veau", arrondissement="Anse-a-Veau"),
            Commune(name="Arnaud", arrondissement="Anse-a-Veau"),
            Commune(name="L'Asile", arrondissement="Anse-a-Veau"),
            Commune(name="Petit-Trou-de-Nippes", arrondissement="Anse-a-Veau"),
            Commune(name="Plaisance-du-Sud", arrondissement="Anse-a-Veau"),
        ),
    )
    baraderes = Arrondissement(
        name="Baraderes",
        communes=(
            Commune(name="Baraderes", arrondissement="Baraderes"),
            Commune(name="Grand-Boucan", arrondissement="Baraderes"),
        ),
    )
    return Department(
        name="Nippes",
        capital="Miragoane",
        arrondissements=(miragoane, anse_a_veau, baraderes),
    )


def iter_communes(department: Department | None = None) -> Iterable[Commune]:
    """Iterate over communes in the working Nippes geography model."""
    target = department or build_nippes_department()
    return iter(target.communes())
