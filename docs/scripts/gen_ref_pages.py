"""Generate one API reference page per module in src."""

from pathlib import Path

import mkdocs_gen_files

LIB_DIR = Path("src")

nav = mkdocs_gen_files.Nav()

for path in sorted(LIB_DIR.rglob("*.py")):
    module_path = path.relative_to(LIB_DIR).with_suffix("")
    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = module_path.parent / "index.md"
    else:
        doc_path = module_path.with_suffix(".md")

    if not parts:
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(Path("reference", doc_path), "w") as fd:
        fd.write(f"::: {'.'.join(parts)}\n")

    mkdocs_gen_files.set_edit_path(Path("reference", doc_path), path)

with mkdocs_gen_files.open("reference/index.md", "w") as fd:
    fd.write("# API Reference\n\n")
    fd.write("Generated from the docstrings of the modules in `src`.\n")

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.write("* [Overview](index.md)\n")
    nav_file.writelines(nav.build_literate_nav())
