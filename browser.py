from pathlib import Path
from playwright.sync_api import sync_playwright, Error as PlaywrightError

BROWSER_PROFILE = Path.cwd() / ".mybot_browser_profile"
BROWSER_PROFILE.mkdir(exist_ok=True)

_playwright = None
_context = None
_page = None

def _is_alive():
    try:
        if _page is None:
            return False
        _page.url
        return True
    except Exception:
        return False

def _launch():
    global _playwright, _context, _page
    if _is_alive():
        return _context, _page

    try:
        if _context:
            _context.close()
    except Exception:
        pass

    try:
        if _playwright:
            _playwright.stop()
    except Exception:
        pass

    _playwright = sync_playwright().start()
    _context = _playwright.chromium.launch_persistent_context(
        user_data_dir=str(BROWSER_PROFILE),
        headless=False,
    )
    _page = _context.new_page()
    return _context, _page

def open_url(url: str):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    _, page = _launch()
    try:
        page.goto(url, wait_until="domcontentloaded")
    except PlaywrightError:
        _, page = _launch()
        page.goto(url, wait_until="domcontentloaded")
    return f"Opened {url}"
