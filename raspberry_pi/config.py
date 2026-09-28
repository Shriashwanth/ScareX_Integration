"""
ScareX Integrated System - Raspberry Pi Edge Node Configuration
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Network Ports
CAMERA_PORT = int(os.getenv("SCAREX_PI_CAMERA_PORT", 8000))
COMMAND_PORT = int(os.getenv("SCAREX_PI_COMMAND_PORT", 9000))

# Camera Settings
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
CAMERA_FPS = 30
JPEG_QUALITY = 80
USB_CAM_INDEX = int(os.getenv("SCAREX_USB_CAM_INDEX", 0))

# Hardware GPIO Pin Configuration (BCM numbering)
# Customize these pins if your wiring differs
GPIO_PINS = {
    # DC Motors (H-Bridge L298N / TB6612)
    "motor_left_forward": 17,
    "motor_left_backward": 27,
    "motor_right_forward": 22,
    "motor_right_backward": 23,
    
    # Ultrasonic Distance Sensor (HC-SR04)
    "ultrasonic_trigger": 24,
    "ultrasonic_echo": 25,
    
    # Pan/Tilt or Camera Servo
    "servo_camera": 18,
    
    # Optional Status Indicator LEDs & Buzzer
    "led_status": 5,
    "led_scare": 6,
    "buzzer": 12
}

# Safety & Watchdog Settings
# If the laptop does not send a command or heartbeat within this timeout,
# the Pi automatically forces all motors and actuators into a safe stopped state.
WATCHDOG_TIMEOUT = 3.0  # seconds

# Deterrence Audio Settings
AUDIO_DIR = os.path.join(BASE_DIR, "assets", "audio")
DETERRENT_DIR = os.path.join(BASE_DIR, "assets", "deterrent_sounds")
SPEAKER_VOLUME = 1.0  # 0.0 to 1.0
AUDIO_COOLDOWN_SECONDS = 5.0

# The 5 Uploaded Bioacoustic Predator Deterrence Sounds
DETERRENT_SOUNDS = [
    {"id": 1, "name": "Monster Roar", "file": "deterrent_1.wav", "orig": "audiopapkin-monster-roar-ps-oo6-306402.mp3"},
    {"id": 2, "name": "Monster Warrior Roar", "file": "deterrent_2.wav", "orig": "dffdv-monster-warrior-roar-195877.mp3"},
    {"id": 3, "name": "Epic Dragon Roar", "file": "deterrent_3.wav", "orig": "dragon-studio-epic-dragon-roar-364481.mp3"},
    {"id": 4, "name": "Spooky Wolf Howl", "file": "deterrent_4.wav", "orig": "dragon-studio-spooky-wolf-howl-410547.mp3"},
    {"id": 5, "name": "Beast Screaming", "file": "deterrent_5.wav", "orig": "freesound_community-beast-human-screaming-86831.mp3"}
]

# Species specific mapping + dynamic alternating mode
SPECIES_AUDIO_MAP = {
    "crow": "deterrent_3.wav",                 # Epic Dragon Roar
    "pigeon": "deterrent_4.wav",               # Wolf Howl
    "sparrow": "deterrent_1.wav",              # Monster Roar
    "common myna": "deterrent_2.wav",          # Warrior Roar
    "myna": "deterrent_2.wav",
    "rose ringed parakeet": "deterrent_5.wav", # Beast Scream
    "parakeet": "deterrent_5.wav",
    "parrot": "deterrent_5.wav",
    "peacock": "deterrent_2.wav",              # Warrior Roar
    "bird": "alternate",                       # Alternate across the 5 sounds
    "default": "alternate"
}
