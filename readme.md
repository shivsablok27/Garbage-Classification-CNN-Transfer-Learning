# ♻️ Trash Classification Web App using Deep Learning (MobileNetV2 + Flask)

A real-time web app that classifies trash images into six categories using deep learning and transfer learning with MobileNetV2. The project also includes a beautiful and interactive frontend where users can either **upload an image** or **capture a photo using the camera**, and instantly get the trash category prediction.

---

## 🧠 Introduction

This project aims to solve a real-world problem — **automated trash classification** — by using **Convolutional Neural Networks (CNNs)** and **Transfer Learning**. The application can distinguish between different types of waste such as plastic, glass, metal, etc., making it useful for smart recycling systems, sustainability initiatives, and waste management.

We have trained a deep learning model using the **MobileNetV2 architecture**, a lightweight CNN optimized for mobile and embedded devices, and deployed it using **Flask**, a lightweight Python web framework.

---

## 🧪 Problem Statement

> Given an input image of trash, classify it into one of the following 6 categories:
- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

---

## 🔬 Deep Learning Approach

### 📌 What is CNN?

A **Convolutional Neural Network (CNN)** is a specialized kind of neural network for processing data with grid-like topology — particularly image data. CNNs automatically learn spatial hierarchies of features through backpropagation by using multiple building blocks, such as:
- Convolutional layers
- Pooling layers
- Fully connected layers

### 📌 What is Transfer Learning?

Instead of training a CNN from scratch, we use **Transfer Learning** where a pre-trained model (MobileNetV2) trained on a massive dataset (ImageNet) is fine-tuned for our trash classification task. This saves time, resources, and leads to better generalization with small datasets.

---

## 🧠 Model Training Details

| Parameter            | Value                         |
|----------------------|-------------------------------|
| Model Architecture   | MobileNetV2 (Keras Applications) |
| Dataset Size         | 2527 images                   |
| Image Size           | 224 x 224                     |
| Classes              | 6 (Cardboard, Glass, Metal, Paper, Plastic, Trash) |
| Data Split           | 2024 train / 503 validation   |
| Framework            | TensorFlow / Keras            |
| Trained on           | Google Colab (GPU)            |
| Saved Model          | `best_model.h5`               |
| Callback             | EarlyStopping + ModelCheckpoint |
| Accuracy Achieved    | ~91% on validation data       |

The model is saved in `.h5` format and is loaded into the Flask app for inference.

---

## 🌐 Web Application

A full-stack web app is created using **Flask (Python)** with HTML/CSS/JavaScript frontend.

### 🔧 Features

- 📸 Capture Image using Device Camera
- 📁 Upload Image from File System
- 🔍 Real-time Prediction using Trained DL Model
- 🎨 Beautiful & Responsive UI (Mobile-friendly)
- ✅ Category Output + Confidence Score
- 🔲 Image Preview with Border
- 🖱️ Predict Button with Hover Effects

---

## 📂 Folder Structure

project/
│
├── static/
│ └── (JS/CSS if separated)
├── templates/
│ └── index.html
├── best_model.h5
├── app.py
├── requirements.txt
└── README.md

---

## 👨‍💻 Developed By

**Shiv Sablok**  
🎓 Aspiring Data Scientist  
---
