# NEURAL-STYLE-TRANSFER

COMPANY NAME : CODTECH IT SOLUTIONS
NAME : SYED FARHANUDDIN SAIF
INTERN ID : CTIS6987
DOMAIN : ARTIFICIAL INTELLIGENCE
DURATION: 4 WEEKS
MENTOR: NEELA SANTOSH

---

# 🎨 Neural Style Transfer System

> 🚀 Deep Learning-based Artistic Image Transformation using VGG19 (PyTorch)

---

## 📌 Table of Contents

* Overview
* Problem Statement
* Objective
* Features
* Tech Stack
* Project Architecture
* Project Structure
* Installation
* Usage
* How It Works
* Results (Examples)
* Performance & Limitations
* Future Enhancements
* Applications
* Conclusion
* Output Preview

---

## 📖 Overview

Neural Style Transfer (NST) is a deep learning technique that blends two images:

* **Content Image** → The structure (e.g., a photograph)
* **Style Image** → The artistic appearance (e.g., a painting)

This project implements NST using a **pre-trained VGG19 convolutional neural network**, enabling the transformation of ordinary images into visually stunning artworks.

---

## ❓ Problem Statement

Traditional image editing tools require manual effort and artistic skill to apply styles. The goal of this project is to:

> Automatically generate artistic images by combining the **content of one image** with the **style of another** using deep learning.

---

## 🎯 Objective

* Implement Neural Style Transfer using PyTorch
* Use pre-trained CNN features for style and content extraction
* Generate high-quality stylized images
* Build a modular and reusable system

---

## ✨ Features

* 🎨 Apply artistic styles to any image
* 🧠 Uses **pre-trained VGG19 model**
* ⚡ Fully implemented in PyTorch
* 🖼️ Supports custom input images
* 🔁 Iterative optimization-based approach
* 🧩 Clean and modular architecture
* 📸 Generates high-resolution stylized outputs

---

## 🧠 Tech Stack

| Technology  | Purpose                 |
| ----------- | ----------------------- |
| Python      | Core programming        |
| PyTorch     | Deep learning framework |
| Torchvision | Pre-trained models      |
| PIL         | Image processing        |
| NumPy       | Numerical operations    |

---

## 🏗️ Project Architecture

```
Input Images (Content + Style)
        │
        ▼
Pre-trained VGG19 Network
        │
        ├── Content Feature Extraction
        ├── Style Feature Extraction (Gram Matrix)
        │
        ▼
Loss Calculation
(Content Loss + Style Loss)
        │
        ▼
Optimization (Gradient Descent)
        │
        ▼
Generated Styled Image
```

---



## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/neural-style-transfer.git
cd neural-style-transfer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---



## 🔬 How It Works

### 1. Feature Extraction

* Uses **VGG19 pre-trained model**
* Extracts features from multiple convolution layers

---

### 2. Content Representation

* Captures the structure of the content image
* Uses deeper layer features (e.g., `conv4_1`)

---

### 3. Style Representation

* Uses **Gram Matrix** to capture texture and patterns
* Extracted from multiple layers

---

### 4. Loss Function

Total Loss =

* Content Loss + Style Loss

Where:

* Content Loss → preserves structure
* Style Loss → transfers artistic features

---

### 5. Optimization

* Starts with a copy of content image
* Updates pixels using gradient descent
* Iteratively improves output

---

## 📸 Results (Examples)

### 🔹 Content Image

![Content](assets/content.jpg)

---

### 🔹 Style Image

![Style](assets/style.jpg)

---

### 🔹 Output Image

![Output](assets/output.jpg)

---

## 📊 Performance & Limitations

### ✅ Strengths

* Produces high-quality artistic outputs
* Flexible for different styles
* Works with any image

### ❌ Limitations

* Slow on CPU (takes several minutes)
* High memory usage
* Requires parameter tuning
* Not real-time

---

## 💡 Future Enhancements

* ⚡ Fast Neural Style Transfer (real-time)
* 🎥 Video style transfer
* 🌐 Web UI (Streamlit / React)
* 🤖 GAN-based style transfer
* ☁️ Cloud deployment

---

## 🌍 Applications

* Digital Art Creation 🎨
* Photo Editing Apps 📸
* Social Media Filters 📱
* Gaming & Animation 🎮
* Film Industry 🎬

---

## 🧠 Design Philosophy

> This project demonstrates the intersection of **deep learning and creativity**, transforming mathematical representations into artistic outputs.

---

## 📸 Output Preview

Example generated output:

```text
Content Image: Natural landscape
Style Image: Van Gogh painting
Output: Artistic landscape with brush stroke patterns
```

Add your screenshot here:

```markdown
![Neural Style Transfer Output](assets/output.png)
```

---

## ❤️ Built With

* PyTorch 🔥
* Python 🐍
* Deep Learning 🧠


# 🔥 WE CAN ALSO SAY IT AS

**Neural Style Transfer using VGG19 for Artistic Image Generation with PyTorch**

---

# 🚀 Final Note

This is not just a project — it shows:

* Deep learning understanding
* Computer vision skills
* Practical AI implementation
* OUTPUT
* <!-- Uploading "Neural style transfer_ lakeside to Van Gogh.png"... -->


