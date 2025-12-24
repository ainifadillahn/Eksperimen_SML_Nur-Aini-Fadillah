**Early Warning System for Machine Failure**
Sistem machine learning untuk mendeteksi risiko kegagalan mesin industri secara dini menggunakan data sensor, memungkinkan maintenance preventif sebelum kerusakan terjadi.

**📋 Deskripsi Project**
Project ini mengimplementasikan sistem prediksi kegagalan mesin yang tidak hanya menghasilkan klasifikasi "rusak/tidak rusak", tetapi memberikan probabilitas kegagalan dan risk level untuk mendukung pengambilan keputusan maintenance.


Output Sistem
json{
  "failure_probability": 0.67,
  "risk_level": "CRITICAL",
  "recommended_action": "Immediate maintenance"
}

**Risk Level Mapping**
ProbabilitasStatusTindakan
< 0.3 Normal Operasi aman
0.3 - 0.6 Warning Perlu inspeksi
> 0.6 CriticalMaintenance segera


**🗂️ Struktur Repository**
Workflow-CI-NurAini/
├── MLProject/
│   ├── modelling.py
│   ├── MLproject
│   ├── conda.yaml
│   └── ai4i2020_preprocessed.csv
├── Monitoring dan Logging/
│   ├── 1.bukti_serving.png
│   ├── 2.prometheus.yml
│   ├── 3.prometheus_exporter.py
│   ├── 7.inference.py
│   ├── 4.bukti monitoring Prometheus/
│   ├── 5.bukti monitoring Grafana/
│   └── 6.bukti alerting Grafana/
└── .github/workflows/
    └── main.yml

**📊 Dataset**
AI4I 2020 Predictive Maintenance Dataset (UCI Machine Learning Repository)
Fitur:

Type: Tipe produk (L/M/H)
Air temperature [K]: Suhu lingkungan
Process temperature [K]: Suhu proses mesin
Rotational speed [rpm]: Kecepatan putaran
Torque [Nm]: Beban kerja mesin
Tool wear [min]: Keausan alat

Target: Machine failure (0 = Normal, 1 = Gagal)

**🚀 Teknologi yang Digunakan**
ML Framework: Scikit-learn, MLflow
CI/CD: GitHub Actions
Containerization: Docker
Monitoring: Prometheus, Grafana
Deployment: MLflow Model Serving

**📦 Instalasi & Setup**
1. Clone Repository
bashgit clone https://github.com/yourusername/Workflow-CI-NurAini.git
cd Workflow-CI-NurAini
2. Setup Virtual Environment
bashpython -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
3. Install Dependencies
bashpip install -r requirements.txt
4. Serve Model
bashcd MLProject
mlflow models serve -m "mlruns/.../artifacts" -h 0.0.0.0 -p 5001 --no-conda
🔄 CI/CD Pipeline
Workflow otomatis di-trigger saat push ke main:

Training: Model dilatih ulang dengan MLflow
Tracking: Metrics & artifacts disimpan
Docker Build: Image dibuat dengan Dockerfile
Push: Image di-push ke Docker Hub


**Alerting Rules:**

High risk machines > threshold
Model latency > 2 seconds
Error rate > 5%

**🐳 Docker**
Pull dan jalankan model:
bashdocker pull ainifadillahn/ai4i2020-model:latest
docker run -p 5001:8080 ainifadillahn/ai4i2020-model:latest

📞 API Endpoint
Health Check
bashcurl http://localhost:5001/health

Prediction
bashcurl -X POST http://localhost:5001/invocations \
  -H "Content-Type: application/json" \
  -d '{
    "dataframe_split": {
      "columns": ["Type", "Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"],
      "data": [[2, 298.1, 308.6, 1551, 42.8, 50]]
    }
  }'


**👤 Author**
Nur Aini Fadillah

GitHub: @ainifadillahn
Docker Hub: ainifadillahn/ai4i2020-model

**📄 License**
This project is created for educational purposes as part of Machine Learning Operations course Asah Dicoding.