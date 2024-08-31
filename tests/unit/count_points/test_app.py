import unittest
import pytest
import re
from count_points import app

platform_name_pattern = re.compile("^[- .a-zA-Z0-9_/()',!]+$")
provider_name_pattern = re.compile("^[a-zA-Z0-9 ,]+$")
date_pattern = re.compile("^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$")
unique_id_pattern = re.compile("^[a-zA-Z0-9-]+$")


class TestApp:
    def test_valid_bbox(self):
        assert app.valid_bbox([-180, -90, 180, 90]) is True, "coordinates should be in range"
        assert app.valid_bbox([-180, -90, 180, 91]) is False, "coordinates should be out of range"
        assert app.valid_bbox([-181, -90, 180, 90]) is False, "coordinates should be out of range"
        assert app.valid_bbox([170, 0, -170, 10]) is False, "bbox crosses the antimeridian"
        assert app.valid_bbox([-10, -10, -10, -10]) is False, "bbox area is zero"

    def test_create_sql_from_bbox_with_out_of_range_coords(self):
        with pytest.raises(app.IllegalArgumentException):
            app.create_sql_from_bbox("-180,-90,180,901")

    def test_create_sql_from_bbox_with_non_numeric_coords(self):
        with pytest.raises(app.IllegalArgumentException):
            app.create_sql_from_bbox("null,-90,180,90")

    def test_create_sql_from_bbox(self):
        expected = [
            '(lon > -180.0 and lon < 180.0)',
            '(lat > -90.0 and lat < 90.0)'
        ]
        bbox_string = '-180, -90, 180, 90'
        assert app.create_sql_from_bbox(bbox_string) == expected

    def test_filters_to_where_clause(self):
        expected = [
            "platform_name in ('Ramform Vanguard','Anonymous')",
            "provider in ('PGS','MacGregor')",
            "time >= date('2022-01-01')",
            "entry_date >= date('2022-01-01')"
        ]
        query_params = {
            "providers": "PGS,MacGregor",
            "platforms": "Ramform Vanguard,Anonymous",
            "collection_date_start": "2022-01-01",
            "archive_date_start": "2022-01-01"
        }
        assert app.filters_to_where_clause(query_params) == expected

    def test_platform_names(self):
        bad_names = [
            '"Airwaves "',
            'ANNIE O&apos;SHEA',
            'Sea &#32;Dweller'
        ]

        good_names = [
            'S_V_Freedom',
            'S/V Aphrodite',
            'St. Dominick',
            "Taylor'd For 2",
            'COMIT 2 - Rescue 5 (Eckerd College)',
            'HALLELUJAH!'
        ]

        for i in bad_names:
            assert platform_name_pattern.match(i) is None, "should reject invalid character(s) in platform name"
        assert platform_name_pattern.match(', '.join(bad_names)) is None, "should reject invalid character(s) in platform name"
        assert platform_name_pattern.match(','.join(bad_names)) is None, "should reject invalid character(s) in platform name"

        for i in good_names:
            assert platform_name_pattern.match(i), "should accept valid character(s) in platform name"
        assert platform_name_pattern.match(', '.join(good_names)), "should accept valid character(s) in platform name"
        assert platform_name_pattern.match(','.join(good_names)), "should accept valid character(s) in platform name"

    def test_provider_names(self):
        good_names = [
            'Anonymous',
            'AquaMap',
            'CIDCO',
            'COMIT USF',
            'FarSounder',
            'GLOS',
            'M2Ocean',
            'MacGregor',
            'Orange Force Marine',
            'PGS',
            'Rosepoint',
            'SB2030',
            'SeaKeepers'
        ]
        for i in good_names:
            assert provider_name_pattern.match(i), "should accept valid character(s) in provider name"
        assert provider_name_pattern.match(', '.join(good_names)), "should accept valid character(s) in provider name"

    def test_unique_id_whitelist(self):
        bad_names = [
            'PGS 83e03090-0999-11eb-b6ea-98be942a5b5a',
            'PGS_83e03090-0999-11eb-b6ea-98be942a5b5a'
        ]
        #
        good_names = [
            'PGS-83e03090-0999-11eb-b6ea-98be942a5b5a'
        ]
        for i in bad_names:
            assert unique_id_pattern.match(i) is None, "should reject invalid character(s) in unique_id"

        for i in good_names:
            assert unique_id_pattern.match(i), "should accept valid character(s) in unique_id"

    def test_date_whitelist(self):
        bad_names = [
            '2008',
            '2008-01',
            'abcd-ef-gh',
            '200&-01-02'
        ]
        good_names = [
            '2008-01-02',
            '2008-1-2'
        ]
        for i in bad_names:
            assert date_pattern.match(i) is None, "should reject dates with invalid characters or format"

        for i in good_names:
            assert date_pattern.match(i), "should accept dates with valid character(s) and format"


if __name__ == '__main__':
    unittest.main()
