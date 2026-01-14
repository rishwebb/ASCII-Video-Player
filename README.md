# ASCII-to-Terminal Video Player

A lightweight Python script developed by **Rishav Biswas** that converts any video file into a real-time ASCII art stream directly inside your terminal. The project is optimized for **15-inch laptop screens**, delivering a near full-screen experience without vertical scrolling, and runs in an **infinite playback loop**.

---

## 🚀 Features

* **Infinite Playback Loop**
  Automatically restarts the video once it ends, creating a continuous ASCII stream.

* **Screen-Size Optimized**
  Uses a custom **1:4.0 vertical scaling ratio** designed specifically for standard 15-inch laptop displays, preventing frame breaks or vertical scrolling.

* **Dynamic Width & FPS Control**
  Manually set terminal character width and frame rate, or rely on smart defaults (recommended **130 width**).

* **Completely Free & Open Source**
  Built entirely using free, open-source Python libraries.

---

## 🛠️ Prerequisites

Make sure Python (3.8+) is installed on your system. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📂 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Add Your Video

Place the video file you want to render (for example, `vid.mp4`) in the same directory as `index.py`.

---

## 📖 Usage

1. Open your terminal or command prompt inside the project folder.
2. Run the script:

```bash
python index.py
```

3. Follow the prompts:

* **Video Path**: Enter the video filename (for example, `vid.mp4`).
* **Terminal Width**: Press **Enter** to use the default `130` (optimized for 15-inch screens).
* **FPS**: Press **Enter** to match the original video frame rate.

To stop playback at any time, press **Ctrl + C**.

> 💡 Tip: For the best visual clarity, slightly zoom out your terminal (Ctrl + -) so the ASCII characters have enough space to render cleanly.

---

## 📦 requirements.txt

```text
opencv-python
numpy
```

---

## 👤 Credits

**Developer**: Rishav Biswas
**Built With**: Python, OpenCV, NumPy
