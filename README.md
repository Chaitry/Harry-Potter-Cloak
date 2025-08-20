🧙‍♂️ Harry Potter Invisibility Cloak 🪄


📌 Project Description-
This project uses OpenCV and NumPy to create an invisibility cloak effect similar to the one from the Harry Potter movies. It detects a specific cloak color in real-time and seamlessly replaces it with the background, making the wearer appear invisible.


✨ Features-
🎥 Real-time video processing using OpenCV
🎨 Color detection with HSV masking
🧩 Background replacement to simulate invisibility
⚡ Optimized performance for smooth output
🛠️ Beginner-friendly implementation


🛠️ Tech Stack Used-
Programming Language: Python 🐍
Libraries & Tools:
OpenCV
 — for video capture and image processing
NumPy
 — for numerical computations and array manipulations


🔄 Project Flow
Capture Background 🎥
The program records a few frames of the background before the cloak is introduced.
Detect Cloak Color 🎨
Convert the video frames from BGR to HSV color space for better color segmentation.
Define a specific HSV color range for the cloak (e.g., red).
Create a Mask 🧩
Generate a binary mask where the cloak color is detected.
Refine the mask using morphological transformations to reduce noise.
Replace Cloak Area with Background 🪄
Use bitwise operations to replace the cloak region with the pre-captured background.
Display Final Output 👀
Combine the processed frames and show the real-time invisibility effect.
