GeoIP2 / MaxMind DB migration notes

This project has migrated from the legacy libgeoip (GeoIP.dat) to MaxMind DB (GeoIP2/.mmdb).

What changed:
- System packages: `libgeoip-dev` / `libgeoip1` replaced by `libmaxminddb-dev` / `libmaxminddb0` in the Dockerfile.
- Python: `geoip2` Python package is installed into the ModSecurity venv during build.
- A helper script `check_geoip.py` was added; it looks for the DB at `/usr/share/GeoIP/GeoLite2-Country.mmdb` or the path in `GEOIP2_DB` env var.

Database (MMDB) handling:
- The image does not automatically include a GeoLite2 database due to licensing and account requirements. Provide a `.mmdb` file by either:
  - Mounting it at runtime (e.g., `-v /path/to/GeoLite2-Country.mmdb:/usr/share/GeoIP/GeoLite2-Country.mmdb`), or
  - Adding a build step that downloads the file using your MaxMind license key and places it at `/usr/share/GeoIP/GeoLite2-Country.mmdb`.

Example runtime test (after starting container):

```bash
python3 /app/check_geoip.py
```

If you want, I can add an optional Docker build-arg to download the GeoLite2 DB at build time (requires `MAXMIND_LICENSE_KEY`), or implement a startup script that downloads/updates the DB if a license key is provided.
