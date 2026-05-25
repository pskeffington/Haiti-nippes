from haiti_nippes.geography import build_nippes_department, normalize_name


def test_build_nippes_department_has_expected_structure():
    department = build_nippes_department()

    assert department.name == "Nippes"
    assert department.capital == "Miragoane"
    assert len(department.arrondissements) == 3
    assert len(department.communes()) == 11


def test_find_commune_matches_hyphen_variants():
    department = build_nippes_department()

    commune = department.find_commune("Petit Trou de Nippes")

    assert commune is not None
    assert commune.name == "Petit-Trou-de-Nippes"


def test_normalize_name_casefolds_and_removes_extra_spacing():
    assert normalize_name("  PETIT-TROU   DE-NIPPES ") == "petit trou de nippes"
