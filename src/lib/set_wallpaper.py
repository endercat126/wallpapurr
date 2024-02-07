# library to set wallpapers on (most) operating systems

import os
import sys
import subprocess
import platform
import logging


logger = logging.getLogger(__name__)

# Set the wallpaper using various native tools
def set_wallpaper(img_path: str):
    if platform.system() == "Windows":
        # Michaelsoft Binblows
        logger.debug("Setting wallpaper using ctypes")  

        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(img_path), 0)

    elif platform.system() == "Darwin":
        # bro thinks he's rich XD
        logger.debug("Using osascript to set wallpaper")

        os.system(f"osascript -e 'tell application \"System Events\" to set picture of every desktop to \"{img_path}\"'")

    elif platform.system() == "Linux":
        # Hurr durr I'ma ninja sloth
        # There are numerous desktop environments, each with their own stupid way of doing this

        if os.environ["XDG_CURRENT_DESKTOP"] == "KDE":
            # Koolaid Desktop Environment
            logger.debug("Using kwriteconfig5 to set wallpaper")

            os.system(f"qdbus-qt5 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{os.path.abspath(img_path)}\")}}\'")

        elif os.environ["XDG_CURRENT_DESKTOP"] == "GNOME":
            # Toes
            logger.debug("Using gsettings to set wallpaper")

            os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{os.path.abspath(img_path)}")

        elif os.environ["XDG_CURRENT_DESKTOP"] == "Cinnamon":
            # Minty Toothpaste
            logger.debug("Using gsettings to set wallpaper")

            os.system(f"gsettings set org.cinnamon.desktop.background picture-uri file://{os.path.abspath(img_path)}")

        elif os.environ["XDG_CURRENT_DESKTOP"] == "XFCE":
            # Mischeivous Mice
            logger.debug("Using xfconf to set wallpaper")

            os.system(f"xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s {os.path.abspath(img_path)}")

        else:
            # Not using a known desktop environment
            # Probably a WM or something

            if os.environ["XDG_SESSION_TYPE"] == "wayland":
                # UwU wayland
                try:
                    logger.debug("Using swww to set wallpaper")

                    subprocess.run(["swww", "init"])
                    subprocess.run(["swww", "img", img_path, "--transition-type", "grow", "--transition-duration", "3"])
                except:
                    try:
                        logger.debug("Using swaybg to set wallpaper")

                        subprocess.run(["swaybg", "-i", os.path.abspath(img_path), "-m", "fill"], check=True)
                    except:
                        logger.warn("No wallpaper tool found.")

            elif os.environ["XDG_SESSION_TYPE"] == "x11":
                # its 2024 why are you still using x11
                try:
                    logger.debug("Using feh to set wallpaper")

                    os.system(f"feh --bg-scale {os.path.abspath(img_path)}")
                except:
                    logger.warn("No wallpaper tool found.")
            
            else:
                logger.warn("Unsupported session type")
    
    else:
        logger.warn("Unsupported operating system")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    set_wallpaper("default_wallpapers/alena-aenami-lost-in-between.jpg")
