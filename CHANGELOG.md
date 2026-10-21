# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Unreleased

### Added

- Documentation organized into Getting started, Guides, Explanation, API Reference, Development
  and Changelog.
- The release tag is shown next to the site name.
- Home page cards, breadcrumbs, a table of contents that follows the reading position and a
  button to view the source of each page.
- Glossary: abbreviations such as CAGR show their meaning on hover.
- Broken anchors in links are reported by the build.

### Changed

- Ultra Tendency logo and favicon.

### Fixed

- Mermaid diagrams and fonts are bundled in the release zip, so they render without internet.

### Removed

- The `mkdocs-section-index` plugin, which did the same as Material's `navigation.indexes`.

## [new_features] - 2026-10-21

### Added

- Custom colours, logo and favicon.
- The theme follows the light or dark mode of the operating system.
- Previous and next buttons at the bottom of each page.

## [offline-testing] - 2026-10-20

### Added

- The release zip can be opened from disk: links point at `.html` files and search works
  offline.

## [test] - 2026-10-20

### Added

- `citystats` package: population density and growth, and temperature summaries.
- MkDocs site with an API reference generated from the docstrings.
- CI, and documentation attached as a zip to each GitHub release.

[new_features]: https://github.com/CamiloDiazGomezUT/mkdocs_testing/releases/tag/new_features
[offline-testing]: https://github.com/CamiloDiazGomezUT/mkdocs_testing/releases/tag/offline-testing
[test]: https://github.com/CamiloDiazGomezUT/mkdocs_testing/releases/tag/test
