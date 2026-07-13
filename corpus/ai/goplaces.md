# goplaces — Go client + CLI for Google Places API (New)

# Places & routes, in Go.

A typed Go client and a single-binary CLI for finding places, resolving locations, fetching details and photos, autocompleting input, and running route-aware searches.

## One page per workflow.

Each command supports human-readable output by default and stable JSON with `--json`. Global flags — `--api-key`, `--timeout`, `--no-color`, endpoint overrides — work everywhere.

### search

Places Text Search. Find places by text, type, rating, price, open state, and location bias.

### nearby

Nearby Search. Search around a required latitude, longitude, and radius.

### autocomplete

Autocomplete. Return place and query suggestions from partial input.

### details

Place Details. Address, coordinates, phone, website, hours, photos, reviews, status.

### photo

Photo Media. Turn a Places photo resource name into a media URL.

### resolve

Resolve. Convert free-form location text into candidate place IDs.

### route

Routes · Places. Sample a route and search for places near waypoints.

### directions

Routes. Distance, duration, warnings, steps, units, drive modifiers.

## Install, key, run.

Enable Places API (New). Enable Routes API for `route` and `directions`. Then export one API key — the CLI and Go client both pick it up. Starting with v0.4.5, macOS release archives are hardened-runtime, Developer ID-signed, and notarized. Go toolchain installs report their tagged module version; local builds report `dev`.

### Three steps to your first call

1. Install the binary. Pick Homebrew, `go install`, or grab a release archive.
2. Enable the APIs in Google Cloud. Places API (New) is required. Routes API is needed for `route` and `directions`.
3. Export your key, then run any command.

## Same workflows, typed.

The root package is `github.com/steipete/goplaces`. Requests mirror the CLI concepts and own their field masks. No wrapper layer over a giant generated client — small surface, idiomatic types.

### What you get

- Typed request and response structs. Place, Photo, Route, Step, OpeningHours — all explicit.
- Deterministic field masks. Each request owns the fields it asks Google for. No surprise costs.
- Context everywhere. Honor cancellation, deadlines, and request-scoped values.
- Pluggable HTTP. Inject your own `http.Client` for retries, tracing, or fakes.

## Small surface, clear split.

Two entry points — the CLI and the Go client — share one place and route implementation. Easy to read in an afternoon.

### CLI entry

The thin `main`. Wires up Kong, flags, version info, and exits.

### Commands & output

Per-command Kong structs, renderers, and the `--json` machine output.

### Public client

Typed requests and responses. Owns field masks and retries.

### HTTP & mapping

The actual Places + Routes calls and the JSON → Go mapping.
