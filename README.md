# AI Performance Monitor Dashboard

This project involves the creation of a **dashboard** for analyzing the performance of a remote server during the training of an **artificial intelligence (AI) model**. The dashboard tracks real-time metrics such as **training speed**, **inference speed**, and **model accuracy**, while ensuring secure communication through an **SSH tunnel** and using cryptographic techniques to protect data.

## Main Features

- **Server Performance Monitoring**: Monitoring of server resources such as **CPU** and **GPU** usage during model training.
- **Model Metrics**: Calculation and visualization of **model accuracy**, including metrics like **MSE** (Mean Squared Error) and **F1-Score** for imbalanced classifications.
- **Data Security**: Secure communication with the server via an **SSH tunnel**, using **cryptography** to protect sensitive data during transmission.
- **Interactive Visualization**: Real-time graphical interface with **Dash by Plotly** to display collected metrics and allow live tracking of model and server performance.

## Technologies Used

- **Backend**: Python with libraries like **psutil** for monitoring CPU resources, and **nvidia-smi** for GPU management.
- **Frontend**: **Dash** for creating real-time interactive graphs.
- **Security**: Secure **SSH tunnel** with **Paramiko** for establishing remote connections to the server.
- **Data Collection**: **Prometheus** for gathering and centralizing performance metrics.
- **Cryptography**: Cryptographic techniques to ensure the confidentiality of transmitted data.

## Project Steps

### 1) Secure SSH Connection
Set up a secure SSH connection with the remote server, using **Paramiko** to manage the connection and execute commands remotely.

### 2) Resource Monitoring
- **CPU Monitoring**: Use **psutil** to track CPU usage during model training.
- **GPU Monitoring**: Use **nvidia-smi** to monitor GPU usage and performance.

### 3) Model Performance Metrics Tracking
Collect **model accuracy metrics** such as:
- **MSE** for regression tasks.
- **F1-Score** for imbalanced classification tasks.

### 4) Cryptography
Integrate **cryptographic methods** to secure communications, ensuring the confidentiality of data exchanged over SSH.

### 5) Real-Time Performance Visualization
Create an interactive dashboard with **Dash by Plotly** to visualize:
- **CPU/GPU metrics**.
- **Model results**.
The dashboard will display **interactive graphs** that update in real-time.

## Conclusion

This project provides a comprehensive solution for **monitoring** and **analyzing the performance** of a server running AI models, while ensuring **data security** through an SSH tunnel and cryptographic techniques. The interactive dashboard offers clear, real-time visualization of both **server** and **model performance**, enabling users to effectively track the progress of their AI model training.
