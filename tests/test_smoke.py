# Smoke test added by the CI repair (see .github/workflows/ci.yml).
#
# The rest of this repository cannot run in CI: `connect.py` builds a live
# Huawei Cloud SDK connection from credentials in `globalVariable.py`, and
# `main.py` polls a Git checkout at a hardcoded local path. Neither is
# available on a CI runner, and there is no manifest declaring the third
# party `openstack` package those modules import, so this test exercises the
# one function in the repository that is pure and side-effect free:
# `globalFunc.timestampToTime`.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from globalFunc import timestampToTime


def test_timestamp_to_time_formats_a_known_epoch_seconds_value():
    formatted = timestampToTime(0)
    assert isinstance(formatted, str), f"expected a string, got {formatted!r}"
    assert formatted.count("-") == 2, f"expected a YYYY-MM-DD prefix, got {formatted!r}"
    assert formatted.count(":") == 2, f"expected an HH:MM:SS suffix, got {formatted!r}"
    date_part, time_part = formatted.split(" ")
    year = date_part.split("-")[0]
    assert len(year) == 4 and year.isdigit(), f"expected a 4-digit year, got {formatted!r}"


if __name__ == "__main__":
    test_timestamp_to_time_formats_a_known_epoch_seconds_value()
    print("ok")
