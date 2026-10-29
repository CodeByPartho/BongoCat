<div align="center">

  <h1>🐱 BongoCat Desktop</h1>

  <p><b>Interactive Desktop Bongo-Tapping Cat Animation Built with Pygame</b></p>

  <p>
    An interactive desktop companion application inspired by the viral Bongo Cat meme. Animates paws and synthesizes acoustic bongo sound effects in response to keyboard and mouse clicks in real time.
  </p>

  <p>
    <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10" /></a>
    <a href="https://www.pygame.org"><img src="https://img.shields.io/badge/Pygame-2.5+-FFE873?style=for-the-badge&logo=python&logoColor=black" alt="Pygame" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" /></a>
  </p>

</div>

---

## 📖 Overview

**BongoCat Desktop** is a desktop widget application built using Python and Pygame. It renders the classic Bongo Cat sprite on your screen, featuring a 30 FPS state engine that transitions between an idle breathing state and alternating left/right paw drum strikes with synchronized audio feedback whenever you type or click.

---

## 🚀 Key Features

- 🥁 **Interactive Drum Tapping** — Alternating left and right paw stroke animations mapped to user keystrokes and mouse clicks.
- 🔊 **Synchronized Acoustic Audio** — Low-latency sound playback via `pygame.mixer` triggered on each tap event.
- ⏱️ **State Machine Animation** — Dynamic timer-based recovery transitioning from active drumming back to idle posture.
- 📦 **PyInstaller Portable Packaging** — Bundled assets structure supporting one-command compilation to standalone executables.
- 🎨 **Alpha-Transparent Sprites** — Crisp 2D illustration rendering with transparent background handling.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | [Python 3.10+](https://www.python.org) | Core application execution |
| **Graphics & Audio** | [Pygame 2.5+](https://www.pygame.org) | 2D surface rendering, window management & mixer audio |
| **Packaging** | PyInstaller | Standalone single-file executable compilation |

---

## 💻 Getting Started

### Prerequisites
- **Python**: `>= 3.10`

### Installation & Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CodeByPartho/BongoCat.git
   cd BongoCat
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Bongo Cat**:
   ```bash
   python bongocat/main.py
   ```
   Type any key or click your mouse inside the window to start playing bongos!

---

## 📄 License

This project is licensed under the **[MIT License](LICENSE)**.

---

<p align="center">Made with ❤️ by Partho</p>
