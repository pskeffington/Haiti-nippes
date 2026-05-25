import pytest

from haiti_nippes.scoring import (
    ScoreWeights,
    distance_score,
    quality_from_missing,
    road_penalty_score,
    travel_time_score,
    weighted_index,
)


def test_distance_score_clamps_to_one():
    assert distance_score(50, severe_threshold_km=25) == 1.0


def test_travel_time_score_scales_to_threshold():
    assert travel_time_score(60, severe_threshold_minutes=120) == 0.5


def test_road_penalty_score_scales_multiplier():
    assert road_penalty_score(2.0, severe_multiplier=3.0) == 0.5


def test_weighted_index_ignores_missing_components():
    score = weighted_index(
        {
            "hospital_distance": 1.0,
            "clinic_distance": None,
            "travel_time": 0.0,
            "road_access": None,
            "wash_vulnerability": None,
        },
        weights=ScoreWeights(
            hospital_distance=1.0,
            clinic_distance=1.0,
            travel_time=1.0,
            road_access=1.0,
            wash_vulnerability=1.0,
        ),
    )

    assert score == pytest.approx(0.5)


def test_quality_from_missing():
    assert quality_from_missing({"a": 1, "b": 2}) == "verified"
    assert quality_from_missing({"a": 1, "b": None}) == "provisional"
    assert quality_from_missing({"a": None, "b": None, "c": None}) == "missing"
