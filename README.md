# slide-show-desktop

*You wanted to look at your vacation photos while working, so instead of just opening a browser tab like a normal person, you built this.*

Frameless, floating, Wayland-compatible desktop slideshow. Runs anywhere Linux + pywebview runs. Works best on Hyprland, but hey, not judging your life choices.

## What You'll Need

- **Arch/CachyOS:** `sudo pacman -S python-pywebview webkitgtk-6.0` — one command, like pulling teeth.
- **Debian/Ubuntu:** `sudo apt install python3-pywebview gir1.2-webkit2-4.1` — and then stare at your terminal wondering why you're not on Arch.
- **Fedora:** `sudo dnf install python3-pywebview webkitgtk6.0` — same vibe, different package manager.
- **Other:** figure it out. It's Python. If you can't install `pywebview` you probably shouldn't be here.

## You Wouldn't Download a Desktop Slideshow

```
git clone https://github.com/you/slide-show-desktop
cd slide-show-desktop
mkdir -p ~/.config/desktop-slideshow/images
cp app.py index.html ~/.config/desktop-slideshow/
```

Now fill `~/.config/desktop-slideshow/images/` with your finest JPEGs. Or PNGs. Or WebPs. We don't discriminate. Throw some pictures in there.

```
python3 ~/.config/desktop-slideshow/app.py
```

A black window appears. If it stays black, you probably didn't put images in the folder. Go do that.

## Image Slots

Put your photos here, genius:

![put images here](https://via.placeholder.com/800x200/000000/ffffff?text=Drop+your+images+here+you+absolute+legend)

| Before | After |
|---|---|
| ![empty](https://via.placeholder.com/400x300/333333/ffffff?text=Empty+directory+%F0%9F%98%AD) | ![slideshow](https://via.placeholder.com/400x300/000000/ffffff?text=Working+slideshow+%F0%9F%98%8E) |

## Make It Less Manual (Systemd)

You want it to start when you log in because you're *that* committed to looking at your desktop backgrounds.

Copy the service file and edit the path to where you put the files:

```
mkdir -p ~/.config/systemd/user
cp slideshow.service ~/.config/systemd/user/
# edit ~/.config/systemd/user/slideshow.service and fix the path if needed
systemctl --user daemon-reload
systemctl --user enable --now slideshow.service
```

Check if it's alive (it probably isn't on the first try):

```
systemctl --user status slideshow.service
```

If it failed: you forgot to install `python-pywebview`, you put the wrong path, or the universe hates you. Check the logs:

```
journalctl --user -u slideshow.service -n 30
```

## Hyprland (Fancy Window Rules)

If you use anything other than Hyprland, skip this section and live with a random floating window like a caveman.

Append to `~/.config/hypr/hyprland.conf`:

```
windowrulev2 = float, title:^(DesktopSlideshowDaemon)$
windowrulev2 = size 800 600, title:^(DesktopSlideshowDaemon)$
windowrulev2 = move 100 100, title:^(DesktopSlideshowDaemon)$
windowrulev2 = pin, title:^(DesktopSlideshowDaemon)$
windowrulev2 = noblur, title:^(DesktopSlideshowDaemon)$
```

Then `hyprctl reload` or log out and back in like it's 1998.

## Dragging

Click and drag the window around. It's frameless so there's no title bar to grab. Just click anywhere and drag like you're throwing a tantrum. Only works on the X11/Sway/Hyprland pywebview backends — if you're on GNOME Wayland, well, good luck with that.

## Files

| File | What it does |
|---|---|
| `app.py` | The Python glue that holds this disaster together |
| `index.html` | The CSS/JS slideshow engine. Fades images. Doesn't judge them. |
| `slideshow.service` | systemd unit so you never have to lift a finger again |
