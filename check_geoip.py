#!/usr/bin/env python3
import os
from geoip2.database import Reader

def main():
    db_path = os.environ.get('GEOIP2_DB', '/usr/share/GeoIP/GeoLite2-Country.mmdb')
    if not os.path.exists(db_path):
        print(f'MMDB not found at {db_path}. Set GEOIP2_DB or place the .mmdb there.')
        return 2
    try:
        with Reader(db_path) as r:
            resp = r.country('8.8.8.8')
            print('Lookup OK:', resp.country.iso_code, resp.country.name)
            return 0
    except Exception as e:
        print('Error opening mmdb or lookup failed:', e)
        return 3

if __name__ == '__main__':
    raise SystemExit(main())
