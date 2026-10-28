"""Build list.html (the email-list copy of the registration page) from index.html.

Christa runs two Kajabi forms so each registration is tagged by source: the Ads form on
index.html (/) and the List form here (/list). Edit index.html only, then run:

    python build-list.py

and commit both files. list.html is noindexed so it never competes with the ad page.
"""
from pathlib import Path

ADS_FORM, LIST_FORM = "2149766748", "2149766749"
here = Path(__file__).parent
src = (here / "index.html").read_text(encoding="utf-8")

assert src.count(f"/forms/{ADS_FORM}/embed.js") == 1, "Ads form embed not found exactly once in index.html"
out = src.replace(f"/forms/{ADS_FORM}/embed.js", f"/forms/{LIST_FORM}/embed.js")
out = out.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex, follow">')
assert 'content="noindex, follow"' in out, "robots meta not found in index.html"
out = out.replace("<!DOCTYPE html>", "<!DOCTYPE html>\n<!-- GENERATED from index.html by build-list.py. Do not edit by hand. -->", 1)

(here / "list.html").write_text(out, encoding="utf-8", newline="\n")
print("list.html written")
