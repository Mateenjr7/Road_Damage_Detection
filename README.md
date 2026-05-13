# 🛣️ Road Damage Detection using YOLOv10

An AI-powered computer vision system for detecting and classifying road damages such as potholes and cracks using the YOLOv10 object detection framework.

This project leverages deep learning and real-world annotated datasets to automate road condition monitoring, enabling smarter infrastructure maintenance, safer transportation, and scalable urban road auditing systems.

---

## 🚀 Live Deployment

🔗 https://road-damage-detection-79x5.onrender.com/

---

## 📌 Features

- Real-time road damage detection
- YOLOv10-based object detection pipeline
- Detection of multiple road damage categories
- Bounding box visualization
- Training and inference support
- Custom dataset support
- Scalable for smart city and transportation systems
- High-speed inference for deployment readiness

---

## 🧠 Problem Statement

Manual road inspection is:
- Time-consuming
- Expensive
- Inconsistent
- Unsafe in heavy traffic environments

This project automates road damage identification using deep learning and computer vision to improve:
- Road safety
- Infrastructure maintenance
- Smart transportation systems
- Municipal monitoring efficiency

---

## 🎯 Objectives

- Detect potholes and road cracks automatically
- Reduce dependency on manual inspections
- Enable intelligent road monitoring systems
- Build a scalable AI-based infrastructure solution

---

## 🏗️ System Architecture

```text
Road Image / Video
        │
        ▼
 Image Preprocessing
        │
        ▼
 YOLOv8 Detection Model
        │
        ▼
 Bounding Box Prediction
        │
        ▼
 Damage Classification
        │
        ▼
 Result Visualization
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| YOLOv10 | Object Detection Framework |
| OpenCV | Image Processing |
| PyTorch | Deep Learning Backend |
| NumPy | Numerical Computation |
| Matplotlib | Visualization |
| Roboflow | Dataset Annotation & Management |

---

## 📂 Project Structure

```text
Road_Damage_Detection/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
├── runs/
├── models/
├── data.yaml
├── train.py
├── detect.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains annotated road images with different types of road damages.

### Damage Categories

- Potholes
- Longitudinal Cracks
- Transverse Cracks
- Surface Damage

### Annotation Format

The annotations follow the YOLO format:

```text
<class_id> <x_center> <y_center> <width> <height>
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Mateenjr7/Road_Damage_Detection.git
cd Road_Damage_Detection
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Training the Model

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

---

## 🔍 Running Detection

### Image Detection

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=sample.jpg
```

### Video Detection

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=video.mp4
```

### Webcam Detection

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=0
```

---

## 📈 Model Performance

| Metric | Value |
|---|---|
| mAP@50 | High Accuracy |
| Precision | Optimized |
| Recall | Optimized |
| Inference Speed | Real-time |

> Performance may vary depending on hardware and dataset quality.

---

## 🖼️ Sample Results

### Input Image
- Road surface image containing potholes/cracks

### Output
- Bounding boxes around detected damages
- Damage classification labels
- Confidence scores

---

## 🌍 Real-World Applications

- Smart city infrastructure monitoring
- Autonomous vehicle safety systems
- Municipal road inspection
- Highway maintenance automation
- Transportation analytics
- Civil engineering monitoring systems

---

## 🔮 Future Enhancements

- Mobile application integration
- Live GPS-based damage mapping
- Cloud deployment
- Severity estimation
- Segmentation-based damage analysis
- Drone-based road inspection
- Multi-camera traffic integration

---

## 📚 Research Inspiration

This project is inspired by recent advancements in:
- YOLO-based road damage detection systems
- Smart transportation AI systems
- Automated infrastructure monitoring research :contentReference[oaicite:1]{index=1}

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

### Abdul Mateen

AI & Full Stack Developer  
B.Tech Computer Science Engineering

GitHub: https://github.com/Mateenjr7

---

## ⭐ Support

If you found this project useful:

- Star the repository
- Fork the project
- Share with others

---

## 📬 Contact

For collaboration or queries:

- GitHub Issues
- LinkedIn
- Email Support

---

## 🚦 Project Status

✅ Active Development  
✅ Research & Experimentation  
✅ Deployment Ready Architecture     insert the deployment link to it https://road-damage-detection-79x5.onrender.com/    and make it even more professional
