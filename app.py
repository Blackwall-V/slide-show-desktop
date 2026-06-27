#!/usr/bin/env python3
import webview, json, mimetypes
from pathlib import Path

IMG_DIR = Path.home() / '.config' / 'desktop-slideshow' / 'images'
IMG_DIR.mkdir(parents=True, exist_ok=True)

def collect_images():
    urls = []
    for f in sorted(IMG_DIR.iterdir()):
        if f.is_file():
            mime, _ = mimetypes.guess_type(f)
            if mime and mime.startswith('image/'):
                urls.append(f.as_uri())
    return urls

class _Api:
    def move_by(self, dx, dy):
        win = webview.windows[0]
        win.move(win.x + dx, win.y + dy)

def _on_start():
    webview.windows[0].evaluate_js(
        f'startSlideshow({json.dumps(collect_images())})')

webview.create_window(
    'DesktopSlideshowDaemon',
    str(Path(__file__).resolve().parent / 'index.html'),
    frameless=True, background_color='#000000',
    width=800, height=600, js_api=_Api(),
)
webview.start(func=_on_start)
