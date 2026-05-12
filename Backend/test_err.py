"""Quick sanity check that Ollama is reachable (uses config.OLLAMA_MODEL)."""

import config
import urllib.error
import urllib.request

url = config.OLLAMA_BASE_URL.rstrip("/") + "/api/tags"
try:
    with urllib.request.urlopen(url, timeout=5.0) as r:
        print(f"GET {url} -> {r.status}")
except urllib.error.URLError as e:
    print(f"Ollama not reachable at {url}: {e}")
else:
    print(f"Default model env: OLLAMA_MODEL={config.OLLAMA_MODEL!r}")
