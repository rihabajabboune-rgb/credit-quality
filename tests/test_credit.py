from credit import calculate_risk


# Cas normaux
def test_high_risk():
    result = calculate_risk(1000, 700)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100)
    assert result == "LOW"


# Cas limites
def test_zero_income():
    assert calculate_risk(0, 500) == -1


def test_negative_income():
    assert calculate_risk(-1000, 500) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0) == "LOW"


def test_ratio_exactly_0_3():
    # 300 / 1000 = 0.3 : la condition est "ratio > 0.3", donc on reste dans LOW
    assert calculate_risk(1000, 300) == "LOW"


def test_ratio_exactly_0_6():
    # 600 / 1000 = 0.6 : la condition est "ratio > 0.6", donc on reste dans MEDIUM
    assert calculate_risk(1000, 600) == "MEDIUM"