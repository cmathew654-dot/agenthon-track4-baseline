# Agenthon Track 4 minimal baseline

Model-free packaging demonstration derived from the official Agenthon Track 4
minimal baseline. This adaptation restricts evidence to the citing entity's
manifest-labelled documents (or shared documents) with eligible dates. It refuses
to fabricate a citation when no eligible document remains. Predictions use simple
lexical retrieval and rule-based fallbacks, not a competitive financial model.

Upstream: https://github.com/Agenthon-2026/track4-analysis-public
Revision: eef782bf5a92f4cc9a1a1522d766adde9f8a09a5

Build for linux/amd64 with the included Dockerfile. Runtime interface:
`analyze --task /input/task.json --corpus /input/corpus --out /output/answer.json`.
Mount a complete official unit at `/input` read-only and a writable `/output`.
The image runs as UID/GID 65534 and needs no model API or external network.
Public fixtures are not included in the image or repository.

Application code and adaptations are MIT-licensed; retain LICENSE when copying.
The base image is the official Python 3.13-slim image pinned in Dockerfile.
Python and Debian components keep their own licenses and notices, available inside
the image under `/usr/local/lib/python3.13/LICENSE.txt` and `/usr/share/doc/`.
Base image information: https://hub.docker.com/_/python

Local public-unit checks cover schema, entity alignment, date/citation rules and
non-rankable smoke admissibility. They do not establish production judge results,
forecast quality, leaderboard rank, or server-side acceptance.
