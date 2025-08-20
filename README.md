# 🧙‍♂️ Harry Potter Invisibility Cloak 🪄  
![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

Create your own **Invisibility Cloak** using **OpenCV** and **NumPy**!  
This project replicates the magical cloak from the *Harry Potter* movies by detecting a specific cloak color and replacing it with the **background** in real-time — making you appear **invisible** ✨.

---

## 📑 Table of Contents
- [📌 About](#-about)
- [🎥 Demo](#-demo)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [🔄 Project Flow](#-project-flow)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [💻 Installation](#-installation)
- [🧑‍💻 Usage](#-usage)
- [📊 Results](#-results)
- [🤝 Contributing](#-contributing)
---

## 📌 About
This project is inspired by the **invisibility cloak** from the *Harry Potter* universe.  
Using **computer vision** techniques, it detects a **specific color** in the video feed, creates a **mask**, and replaces the cloak area with a **pre-captured background**, producing a seamless invisibility effect.

---

## 🎥 Demo
> ⚡ *Coming Soon!*    

**Example placeholder for GIF:**  
![Demo GIF](assets/demo.gif)

---

## ✨ Features
- 🎥 **Real-time video processing** with OpenCV  
- 🎨 **Color detection** using HSV masking  
- 🧩 **Background replacement** to simulate invisibility  
- ⚡ **Optimized performance** for smooth, lag-free output  
- 🛠️ **Beginner-friendly** and easy to understand  

---

## 🛠️ Tech Stack
**Programming Language:** [Python 🐍](https://www.python.org/)  

**Libraries & Tools Used:**
- [OpenCV](https://opencv.org/) → Video capture and image processing  
- [NumPy](https://numpy.org/) → Numerical computations and array manipulations  

---

## 🔄 Project Flow
1. **Capture Background** 🎥  
   - Record a few frames of the static background **before** the cloak is introduced.
2. **Detect Cloak Color** 🎨  
   - Convert each video frame from **BGR** to **HSV** color space for effective segmentation.
   - Define a specific **HSV range** for your cloak color.
3. **Create a Mask** 🧩  
   - Generate a binary mask where the cloak color is detected.
   - Refine the mask using **morphological transformations** to reduce noise.
4. **Replace Cloak Area with Background** 🪄  
   - Use **bitwise operations** to blend the background seamlessly over the cloak.
5. **Display Final Output** 👀  
   - Combine processed frames and display the real-time **invisibility effect**.

---

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### ✅ Prerequisites
- **Python** `>=3.6`
- Install required dependencies from `requirements.txt`

### 💻 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/harry-potter-invisibility-cloak.git
   cd harry-potter-invisibility-cloak

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install project dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the project
   ```
   python invisibility_cloak.py
   ```

## Usage
- Wear a cloak of a distinct color (red, green, or blue is recommended).
- Stand in front of the camera without the cloak for a few seconds so the program can capture the background.
- Put on the cloak and watch yourself disappear! 🪄
- Press q to quit the program.

## 📊 Results

- Once you run the program, you’ll observe:
✅ The cloak area replaced by the captured background
✅ Smooth, real-time invisibility effect

	
## 🤝 Contributing

- Contributions are welcome! 🎉
- To contribute: Contributions are always welcome!!! 
Fork the repository ->
Create a new feature branch ->
Submit a pull request 🚀
