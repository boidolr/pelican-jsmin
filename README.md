# pelican-jsmin: A Plugin for Pelican

[![tag](https://img.shields.io/github/v/tag/boidolr/pelican-jsmin?sort=semver)](https://github.com/boidolr/pelican-jsmin/tags)
![python](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fboidolr%2Fpelican-jsmin%2Fmain%2Fpyproject.toml)
[![Build Status](https://img.shields.io/github/actions/workflow/status/boidolr/pelican-jsmin/main.yml?branch=main)](https://github.com/boidolr/pelican-jsmin/actions)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Pelican plugin adding [rjsmin](https://github.com/ndparker/rjsmin) as a template filter to handle inline scripts.
No bundling or dead code elimination is performed.

## Installation

This plugin can be installed via:

    python -m pip install git+https://github.com/boidolr/pelican-jsmin.git@main

As long as you have not explicitly added a `PLUGINS` setting to your Pelican settings file, then the newly-installed plugin should be automatically detected and enabled. Otherwise, you must add `jsmin` to your existing `PLUGINS` list. For more information, please see the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.

## Usage

```
<script>
{%- filter jsmin %}
    {% include "script.js" %}
{% endfilter -%}
</script>
```

## License

This project is licensed under the MIT license.
