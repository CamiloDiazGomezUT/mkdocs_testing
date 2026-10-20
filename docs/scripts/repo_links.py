"""MkDocs hook that points links to files outside docs/ at the repository on GitHub.

The docs link to source files with relative paths such as
``../infrastructure/main.tf`` so that they work when browsing the repository.
Those files are not part of the site, so the links are rewritten at build time.

Links point at the git ref in the ``DOCS_REF`` environment variable (a release tag
such as ``v1.2.0``), or at ``main`` when it is not set.
"""

import os
import re

LINK_PATTERN = re.compile(r"\]\(\.\./(?!docs/)([^)\s#]+)(#[^)\s]*)?\)")


def on_page_markdown(markdown, page, config, files):
    """Rewrite relative links that leave docs/ into GitHub blob links."""
    ref = os.environ.get("DOCS_REF") or "main"
    base_url = f"{config['repo_url'].rstrip('/')}/blob/{ref}/"

    def replace(match):
        return f"]({base_url}{match.group(1)}{match.group(2) or ''})"

    return LINK_PATTERN.sub(replace, markdown)
