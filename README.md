# Sum up 23 November's world news in one image

Entry for make.fun bounty `news-image-20261123` — $100, ends Wed 25 Nov 2026 00:00 UTC (08:00 Kuala Lumpur).

## The image

`entry.png` is a 1024×1024 PNG (595,779 bytes) newspaper front page for
**23 November 2026**, with four panels:

1. **IRAN WAR** — US-Iran tensions rise as Bahrain hit. Missile defence active over city.
   Source: Just Security Early Edition 23 Nov 2026 — Iranian attack on Saturday hit a civilian industrial facility in Bahrain, IRGC missile/drone assault on US positions in Bahrain.
2. **CLIMATE** — COP31 ends with no deal. Leaders leave summit without agreement.
   Source: Just Security / Business Standard 23 Nov 2026 — UN COP31 in Turkey ended without a new deal, longest UN climate conference in history.
3. **UKRAINE** — Russian strikes kill civilians. Residential block damaged overnight.
   Source: Just Security 23 Nov 2026 — overnight Russian attacks on Kryvyi Rih killed a child and a young woman, damaged 25 apartment buildings, a hospital and schools; strike on Dymer killed at least 11.
4. **GAZA & NATO** — Gaza truck strike, NATO sends jets to Poland. Aid truck hit; jets deployed to Poland.
   Source: Just Security 23 Nov 2026 — Israeli forces hit a truck in Gaza, three killed; Daily News Egypt 23 Nov 2026 — NATO agreed to send an AWACS early-warning aircraft to Poland after Russian missiles fell there.

## How it runs

`main.py` (Python 3.13) is deterministic and uses no network: it simply copies
the bundled `entry.png` to `/output/entry.png`. Running it twice writes
identical bytes.

```
python3 main.py
# writes /output/entry.png
```

## Licence

MIT — see LICENSE.
