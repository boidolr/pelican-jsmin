import locale
import pathlib

import pytest

from pelican import Pelican
from pelican.settings import read_settings
from pelican.tests.support import mute

from . import jsmin

CUR_DIR = pathlib.Path(__file__).parent
THEME_DIR = CUR_DIR / "test_data"


@pytest.fixture
def settings(tmp_path):
    """Provide Pelican settings to include test data."""
    override = {
        "PATH": str(CUR_DIR / "test_data"),
        "OUTPUT_PATH": str(tmp_path),
        "PLUGINS": [jsmin],
        "DIRECT_TEMPLATES": ["index"],
        "THEME": str(THEME_DIR),
        "THEME_TEMPLATES_OVERRIDES": [str(THEME_DIR)],
        "SITEURL": "",
        "LOCALE": locale.normalize("en_US"),
        "TIMEZONE": "Europe/Berlin",
        "DEFAULT_DATE": "fs",
        "CACHE_CONTENT": False,
    }
    return read_settings(override=override)


def test_minify(settings, tmp_path):
    """Check that included script is minified after filter execution."""
    pelican = Pelican(settings=settings)
    mute(True)(pelican.run)()

    html = pathlib.Path(tmp_path / "index.html").read_text()
    assert '<script>console.log("Testing!");</script>' in html
