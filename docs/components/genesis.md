# G.E.N.E.S.I.S. - GEneral Nexus for Experimental Software and Informative Scripts (Python Utilities)

<img src="https://www.oasisproject.net/assets/GENESIS_Logo_bg.png" alt="GENESIS Logo" width="350" align="right">

## Overview

G.E.N.E.S.I.S. (GEneral Nexus for Experimental Software and Informative Scripts) is the Python utilities repository for the O.A.S.I.S. ecosystem. It provides computer vision, camera integration, and hardware interaction scripts for Raspberry Pi and NVIDIA Jetson platforms.

GENESIS contains standalone utilities that support development and experimentation across the ecosystem. Each utility is self-contained with its own dependencies and documentation.

Current utilities:
- **Pi ChatGPT Vision Trigger** — Camera-based text detection with GPIO control using OpenAI Vision API
- **Simple PiCamera HUD** — Lightweight heads-up display for Raspberry Pi cameras with real-time overlays
- **Jetson RTSP Server** — RTSP streaming server for NVIDIA Jetson with CSI, USB, and ZED camera support

## Software Dependencies

### Pi ChatGPT Vision Trigger

- Python 3.7+
- pygame 2.6.1, openai 1.12.0, RPi.GPIO 0.7.1, requests 2.31.0, pillow 10.2.0, pyyaml 6.0.1, numpy 1.26.4
- Raspberry Pi with camera module and GPIO
- OpenAI API key

### Simple PiCamera HUD

- Python 3.7+
- pygame, picamera2, numpy
- Raspberry Pi with camera module

### Jetson RTSP Server

- Python 3.7+
- PyGObject, GStreamer 1.0 and plugins, NVIDIA encoder libraries
- NVIDIA Jetson platform
- Optional: ZED SDK (for ZED camera support)

## Installation

Each utility is installed independently within its own directory.

### Pi ChatGPT Vision Trigger

```bash
cd pi_chatgpt_vision_trigger
python -m venv env
source env/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your-api-key-here"
```

### Simple PiCamera HUD

No additional installation required beyond system Python packages (pygame, picamera2, numpy).

### Jetson RTSP Server

```bash
cd jetson_rtsp_server
bash setup.sh        # Installs system dependencies and creates venv
source env/bin/activate
```

The setup script installs GStreamer development libraries, creates a virtual environment, and installs PyGObject bindings. ZED SDK must be installed separately if ZED camera support is needed.

## Configuration

### Pi ChatGPT Vision Trigger

Edit `pi_chatgpt_vision_trigger/config.yaml`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `led_pin` | 17 | GPIO pin for output device (BCM numbering) |
| `screen_width` / `screen_height` | 800 x 600 | Preview window size |
| `camera_width` / `camera_height` | 1920 x 1080 | Native camera capture resolution |
| `capture_interval` | 5 | Seconds between captures |
| `max_image_width` / `max_image_height` | 1920 x 1080 | Maximum dimensions for API submission |
| `trigger_words` | [example, test, detect, word] | Words that trigger GPIO activation |
| `min_api_interval` | 1 | Minimum seconds between API calls |

### Simple PiCamera HUD

Configuration is set in the script source:

```python
camera_resolution = (1920, 1080)
desired_framerate = 30
rotate = 0  # 0, 90, 180, or 270 degrees
```

### Jetson RTSP Server

All settings are passed as command-line arguments (see Usage).

## Usage

### Pi ChatGPT Vision Trigger

```bash
cd pi_chatgpt_vision_trigger
source env/bin/activate
python pi_chatgpt_vision_trigger.py
```

Exit: Press ESC, close window, or Ctrl+C. Logs are written to `vision_trigger.log`.

### Simple PiCamera HUD

```bash
python simple_picamera_hud.py
```

Keyboard controls:
- `E` or `Q` — Quit
- `P` — Shutdown system
- `F` — Toggle fullscreen

### Jetson RTSP Server

```bash
cd jetson_rtsp_server
source env/bin/activate

# CSI camera (default)
python rtsp_server.py --camera csi --width 1920 --height 1080

# USB camera
python rtsp_server.py --camera usb --device-id 0 --width 1280 --height 720

# ZED camera
python rtsp_server.py --camera zed --device-id 0 --width 1920 --height 1080
```

Stream URL: `rtsp://<device-ip>:<port>/camera` (default port 8554).

Command-line options: `--camera`, `--device-id`, `--width`, `--height`, `--framerate`, `--port`, `--bitrate`.

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Camera not detected (Pi) | libcamera not installed or camera disabled | Run `sudo raspi-config` and enable camera interface |
| OpenAI API errors | Invalid or missing API key | Verify `OPENAI_API_KEY` environment variable is set |
| GPIO permission denied | Script not running with GPIO access | Run with `sudo` or add user to `gpio` group |
| Poor text recognition | Image resolution too low or poor lighting | Increase `camera_width`/`camera_height`; improve lighting |
| RTSP stream not accessible | Firewall blocking port | Open port 8554 (or configured port) in firewall |
| GStreamer pipeline error | Missing plugins or encoder | Run `setup.sh` to install dependencies; verify NVIDIA drivers |
| pygame display error | No display connected or X11 not available | Set `SDL_VIDEODRIVER=dummy` for headless, or connect display |
| ZED camera not found | ZED SDK not installed | Install ZED SDK separately from stereolabs.com |
| High API costs | Capture interval too short | Increase `capture_interval` and `min_api_interval` in config |

## Related Components

- [M.I.R.A.G.E.](https://www.oasisproject.net/components/mirage/) - Simple PiCamera HUD shares concepts with the MIRAGE display system
- [D.A.W.N.](https://www.oasisproject.net/components/dawn/) - Vision trigger can interface with DAWN's AI assistant capabilities
- [A.U.R.A.](https://www.oasisproject.net/components/aura/) - Jetson RTSP server can stream camera feeds alongside AURA sensor data
- [B.E.A.C.O.N.](https://www.oasisproject.net/components/beacon/) - CAD models for hardware that runs GENESIS utilities
