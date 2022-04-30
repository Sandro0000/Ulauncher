import os
import mimetypes
from pathlib import Path
from gi.repository import GLib
from os.path import basename, dirname, isdir, join

try:
    from gi.repository import Gtk, Gio
except:
    Gtk, Gio = None, None

DEFAULT_FILE_ICON = "modes/file_browser/images/default_file.png"
DEFAULT_FOLDER_ICON = "modes/file_browser/images/default_folder.png"
IMAGE_EXTENSIONS = (
    '.png',
    '.jpg', '.jpeg',
)

SPECIAL_DIRS = {
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD): 'folder-download',
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOCUMENTS): 'folder-documents',
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_MUSIC): 'folder-music',
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_PICTURES): 'folder-pictures',
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_PUBLIC_SHARE): 'folder-publicshare',
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_TEMPLATES): 'folder-templates',
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_VIDEOS): 'folder-videos',
    GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DESKTOP): 'user-desktop',
    Path('~').expanduser(): 'folder-home'
}


def get_icon_from_path(path, size=256):
    """
    Get the gtk icon path for a specific file or folder (defined by its path).
    """
    if path.lower().endswith(IMAGE_EXTENSIONS):
        return str(path)

    if Gtk is not None:
        try:
            if isdir(path):
                icon = Gio.content_type_get_icon("folder")
            else:
                mimetype = Gio.content_type_guess(Path(path).name)[0]
                icon = Gio.content_type_get_icon(mimetype)

            theme = Gtk.IconTheme.get_default()
            actual_icon = theme.choose_icon(icon.get_names(), size, 0)
            if actual_icon:
                return actual_icon.get_filename()
        except Exception:
            pass

    if isdir(path):
        return DEFAULT_FOLDER_ICON
    else:
        return DEFAULT_FILE_ICON
