"""MkDocs hook that ties the site to the git ref it is built from.

The ref is the ``DOCS_REF`` environment variable (a release tag such as ``v1.2.0``), or
``main`` when it is not set.

- The tag is appended to the site name, so a release zip shows which version it documents.
- The "view source" button of each page points at the ref.
- The docs link to source files with relative paths such as ``../infrastructure/main.tf``
  so that they work when browsing the repository. Those files are not part of the site,
  so the links are rewritten at build time into GitHub links at the ref.
"""

import os
import posixpath
import re

LINK_PATTERN = re.compile(r"\]\(((?:\.\./)+[^)\s#]+)(#[^)\s]*)?\)")


def _docs_ref():
    return os.environ.get("DOCS_REF") or "main"


def on_config(config):
    """Show the release tag in the site name and point the source buttons at it."""
    if os.environ.get("DOCS_REF"):
        config["site_name"] = f"{config['site_name']} {_docs_ref()}"
    config["edit_uri"] = f"blob/{_docs_ref()}/docs/"
    return config


def on_page_markdown(markdown, page, config, files):
    """Rewrite relative links that leave docs/ into GitHub blob links."""
    base_url = f"{config['repo_url'].rstrip('/')}/blob/{_docs_ref()}/"
    repo_root = os.path.dirname(config["config_file_path"])
    docs_dir = os.path.relpath(config["docs_dir"], repo_root).replace(os.sep, "/")
    page_dir = posixpath.join(docs_dir, posixpath.dirname(page.file.src_uri))

    def replace(match):
        target = posixpath.normpath(posixpath.join(page_dir, match.group(1)))
        if target.startswith((f"{docs_dir}/", "../")):
            return match.group(0)
        return f"]({base_url}{target}{match.group(2) or ''})"

    return LINK_PATTERN.sub(replace, markdown)
