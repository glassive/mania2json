# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-08-06

### Added
- Initial release of mania2json
- `mania_file_parser` class for parsing individual .osu files
- `mania_mapset_parser` class for batch processing directorie
- JSON export functionality
- osu!mania 4K maps detection
- Comprehensive beatmap data extraction including:
  - Metadata (title, artist, creator, etc.)
  - Difficulty settings
  - Hit objects with timing
  - Timing points
  - Background information
  - Long note and short note counts

### Features
- Parse osu! v14 file format
- Automatic 4K mania map detection
- Memory-efficient parsing with content cleanup

### Performance
- Multi-threaded folder processing (configurable worker count)
- Lightweight parsing mode for faster validation
- Optimised memory usage
