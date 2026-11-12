# outlanddynamics.com

The Outland Dynamics website, served by GitHub Pages at https://outlanddynamics.com.

- Site files: `index.html` (company), `odin.html` (ODIN product page), `install.html` (ODIN install guide), `support.html`, `privacy.html`, `style.css`, `assets/`.
- Sources: `src/` holds the page bodies and `build.py`, which wraps them in the shared header/footer and renders the privacy policy from `src/privacy-policy.md`.

Rebuild after editing a source file:

```
python3 src/build.py src/privacy-policy.md .
```

Requires Python 3 with the `markdown` package (`pip install markdown`).
