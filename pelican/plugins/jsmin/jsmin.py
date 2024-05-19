"""Pelican plugin to use `rjsmin` to minify JS files."""

import logging

from pelican import signals

try:
    import rjsmin
except ImportError:
    rjsmin = None


def _identity(script):
    return script


def add_jinja2_ext(pelican):
    """Add rjsmin filter to Jinja2 extensions in Pelican settings."""
    minifier = rjsmin.jsmin if rjsmin else _identity
    pelican.settings["JINJA_FILTERS"]["jsmin"] = minifier


def register():
    """Plugin registration."""
    if rjsmin is None:
        logger = logging.getLogger(__name__)
        logger.warning("failed to load 'rjsmin' dependencies")

    signals.initialized.connect(add_jinja2_ext)
