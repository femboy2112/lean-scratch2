# Witness Data Schema

Every witness JSON should include:

```json
{
  "status": "Computational Observation | Verified Fact | Not Established | Advisory Only",
  "target": "string",
  "scope": "finite-level model details",
  "method": "Python | SymPy | Sage | modular probe | numerical probe",
  "claim_boundary": "what this does not prove",
  "reproduction_command": "exact command",
  "input_hashes": {},
  "outputs": [],
  "warnings": [],
  "created_utc": "ISO-8601 timestamp"
}
```

Allowed generated locations:

```text
reports/
data/generated/
```

Do not overwrite old witnesses without preserving hashes or timestamped names.
