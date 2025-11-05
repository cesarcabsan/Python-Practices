# Imagine a graphical user interface (GUI) application where multiple icons of different types (e.g., file icons, folder icons) need to be displayed on a screen. 
# Each icon type has a specific appearance and behavior, such as different images and positions on the screen. 
# However, displaying numerous icons of the same type can consume significant memory if each icon object stores its unique properties independently.

from abc import ABC, abstractmethod

# Flyweight interface
class Icon(ABC):
    @abstractmethod
    def draw(self, x, y):
        pass

# Concrete Flyweight classes for different icons
class FileIcon(Icon):
    def __init__(self, file_type, image_name):
        self.file_type = file_type
        self.image_name = image_name
        
    def draw(self, x, y):
        print(f"Drawing {self.file_type} icon with image {self.image_name} at position ({x}, {y})")
        
class FolderIcon(Icon):
    def __init__(self, color, image_name):
        self.color = color
        self.image_name = image_name
        
    def draw(self, x, y):
        print(f"Drawing folder icon with color {self.color} and image {self.image_name} at position ({x}, {y})")

# Flyweight factory to manage creation and retrieval of flyweight objects
class IconFactory:
    def __init__(self):
        self.icon_cache = {}  # Cache for storing icons

    def get_icon(self, key):
        # Check if the icon already exists in the cache
        if key in self.icon_cache:
            return self.icon_cache[key]
        else:
            # Create a new icon based on the key (type of icon)
            if key == "file":
                icon = FileIcon("document", "document.png")
            elif key == "folder":
                icon = FolderIcon("green", "folder.png")
            else:
                raise ValueError(f"Unsupported icon type: {key}")
            # Store the created icon in the cache
            self.icon_cache[key] = icon
            return icon
        
icon_factory = IconFactory()

# Draw file icons at different positions
file_icon1 = icon_factory.get_icon("file")
file_icon1.draw(100, 100)

file_icon2 = icon_factory.get_icon("file")
file_icon2.draw(150, 150)
 
# Draw folder icons at different positions
folder_icon1 = icon_factory.get_icon("folder")
folder_icon1.draw(200, 200)

folder_icon2 = icon_factory.get_icon("folder")
folder_icon2.draw(250, 250)