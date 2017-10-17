import os
from os.path import join, dirname

import pytest

from pubgis.match import PUBGISMatch
from pubgis.minimap_iterators.images import ImageIterator
from tests.common_test_functions import MOCK_TIME_STEP, generate_list_of_approx_coords

MOCK_WATER_VIDEO = join(dirname(__file__), "water_test")
MOCK_PLANE_VIDEO = join(dirname(__file__), "plane_test")

MOCK_VIDEO_CASES = [
    (MOCK_WATER_VIDEO, generate_list_of_approx_coords(MOCK_WATER_VIDEO)),
    (MOCK_PLANE_VIDEO, generate_list_of_approx_coords(MOCK_PLANE_VIDEO)),
]


@pytest.mark.parametrize("input_minimap_folder, expected_positions", MOCK_VIDEO_CASES)
def test_mock_video(input_minimap_folder, expected_positions):
    mini_iter = ImageIterator(input_minimap_folder, MOCK_TIME_STEP, just_minimaps=True)
    match = PUBGISMatch(mini_iter)

    _, _, unscaled_positions = zip(*match.process_match())

    assert list(unscaled_positions) == list(expected_positions)
