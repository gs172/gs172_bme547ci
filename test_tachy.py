import pytest


@pytest.mark.parametrize("a,expected", [
                                        ("tachycardic", True),
                                        ("TACHYCARDIC", True),
                                        ("Tachycardic", True),
                                        (" tachycardic", True),
                                        ("tachycardic ", True),
                                        ("tachycardic.", True),
                                        ("Tachycardic.", True),
                                        ("Tachycardic ", True),
                                        (" Tachycardic", True),
                                        (" Tachycardic.", True),
                                        ("TACHYCARDIC ", True),
                                        (" TACHYCARDIC", True),
                                        (" TACHYCARDIC.", True),
                                        ("TACHYCARDIC.", True),
                                        ("banana", False),
                                        ])
def test_tachy(a, expected):
    from tachycardia import is_tachycardic
    result = is_tachycardic(a)
    assert result == expected
