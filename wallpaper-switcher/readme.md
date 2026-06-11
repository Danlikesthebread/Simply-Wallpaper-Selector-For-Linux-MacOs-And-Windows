# Animated HUD Wallpaper Selector

A modern, minimalist, and fluid real-time wallpaper changer UI built with a translucent Glassmorphic design using PyQt6.

##Features

Infinite Carousel: Seamless and infinite cyclic navigation through your favorite wallpapers with zero optical cuts.
Glassmorphism Design: Stylized UI featuring advanced drop shadows, dynamic borders, and reactive gradients.
Asynchronous Loading (Multithreading): Background thumbnail processing via QThreadPool to keep the UI running at maximum FPS without freezing.
Real-Time Resilience: Active folder monitoring via QFileSystemWatcher with auto-recovery mechanisms for directory mutation.
Optimized Hybrid Control: Synchronized keyboard and mouse inputs without focus conflicts.

##Prerequisites

Ensure you have Python 3.8 or higher installed along with the required libraries:
pip install PyQt6 Pillow
(Note: Make sure your local modules wallpaper.py and thumbnail_cache.py are placed in the same directory).

##Project Structure

├── main.py                # Entry point to launch the application window
├── selector.py            # HUD User Interface component (with mouse/keyboard focus fix)
├── wallpaper.py           # Core backend functions: get_wallpapers() and apply_wallpaper()
├── thumbnail_cache.py     # Image caching module: create_thumbnail() optimization
└── README.md              # Project documentation


##Usage Guide & Interactions

Note: This project has only been tested on linux mint cinnamon. I am not responsible for any damage that may occur in others OS or environments.
To launch the selector manually, run:
python main.py

##Controls & Shortcuts

### Navigation & Focus

Advance (Right): Right Arrow, D, Down Arrow, S (Keyboard) / Right Arrow Button Click or Scroll Wheel Down (Mouse)
Retreat (Left): Left Arrow, A, Up Arrow, W (Keyboard) / Left Arrow Button Click or Scroll Wheel Up (Mouse)
Focus Card: Direct Left Click on any thumbnail card (Mouse)

###System Actions

Confirm & Apply Wallpaper: Enter / Return key or Double Left Click on the focused thumbnail
Close Window: Escape (Esc) key
##Setting Up a Global System Shortcut (Manual Configuration)
Since this application acts as an overlay launcher, it is best experienced when bound to a global system hotkey. Here is how to configure it manually on your operating system:

Note: This project has only been tested on linux mint cinnamon. I am not responsible for any damage that may occur in others OS or environments.

### Windows Configuration

1. Create a file named launch.bat in your project directory containing the following lines:
   
@echo off
cd /d "C:\path\to\your\project"
python main.py


3. Right-click launch.bat -> Send to -> Desktop (create shortcut).
4. Go to your Desktop, right-click the newly created shortcut and select Properties.
5. Click inside the Shortcut key field and press your preferred hotkey combination (e.g., Ctrl + Alt + W).
6. (Optional) In the "Run" dropdown menu, select Minimized so the command prompt window stays hidden when launching.
   
### Linux Configuration (GNOME / KDE / XFCE / CINNAMON)

1. Open your system Settings and navigate to Keyboard -> Keyboard Shortcuts (or View and Customize Shortcuts).
2. Scroll to the bottom and click on Custom Shortcuts -> Add Shortcut (+).
3. Fill out the configuration prompt:
   
Name: Wallpaper HUD Selector
Command: python3 /path/to/your/project/main.py

5. Click Set Shortcut and press your desired key combination (e.g., Super + W or Ctrl + Alt + W).
6. 
### macOS Configuration

1. Open the built-in Shortcuts application.
2. Click + to create a new shortcut, select Add Action, and search for Run Shell Script.
3. Type the script to execute your script (specifying the absolute path to your python environment and main.py file).
4. In the right-hand sidebar menu, click on the Shortcut Details icon, enable Use as Quick Action, and check Run with Key Combination to assign your global hotkey.
