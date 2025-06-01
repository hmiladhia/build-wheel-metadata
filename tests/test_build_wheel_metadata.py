import build_wheel_metadata


def test_build_wheel_metadata() -> None:
    print(build_wheel_metadata.__version__)
    assert True
