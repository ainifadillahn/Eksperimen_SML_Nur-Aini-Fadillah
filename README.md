# Early Warning System for Machine Failure

Sistem machine learning untuk mendeteksi risiko kegagalan mesin industri secara dini menggunakan data sensor, memungkinkan maintenance preventif sebelum kerusakan terjadi.

## 📋 Deskripsi Project

Proyek ini bertujuan membangun **Early Warning System** berbasis machine learning untuk mendeteksi potensi kegagalan mesin industri menggunakan data sensor.  
Sistem tidak hanya memprediksi apakah mesin gagal, tetapi menghitung **probabilitas kegagalan** sehingga tindakan maintenance dapat dilakukan lebih awal.

**Output Sistem:**

```json
{
  "failure_probability": 0.67,
  "risk_level": "CRITICAL",
  "recommended_action": "Immediate maintenance"
}
```

**Risk Level Mapping:**

| Probabilitas | Status | Tindakan |
|--------------|--------|----------|
| < 0.3 | Normal | Operasi aman |
| 0.3 - 0.6 | Warning | Perlu inspeksi |
| > 0.6 | Critical | Maintenance segera |

## 📊 Dataset

- **Nama:** AI4I 2020 Predictive Maintenance Dataset  
- **Sumber:** https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset  

- **Fitur:**
- Type: Tipe produk (L/M/H)
- Air temperature [K]: Suhu lingkungan
- Process temperature [K]: Suhu proses mesin
- Rotational speed [rpm]: Kecepatan putaran
- Torque [Nm]: Beban kerja mesin
- Tool wear [min]: Keausan alat

**Target:** Machine failure (0 = normal, 1 = gagal)

**Sumber Dataset:** https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset

Dataset berisi data sensor mesin seperti temperatur, kecepatan rotasi, torsi, dan keausan alat yang merepresentasikan kondisi operasional mesin.


## 🗂️ Struktur Repository

```
Eksperimen_SML_Nur-Aini-Fadillah/
├── Eksperimen_SML_Nur-Aini-Fadillah.txt
├── Membangun_model/
│   ├── modelling.py
│   ├── ai4i2020_preprocessed.csv
│   ├── screenshoot_dashboard.jpg
│   ├── screenshoot_artifak.jpg
│   ├── requirements.txt
│   └── MLproject
│       └── conda.yaml
├── Workflow-CI.txt
└── Monitoring dan Logging/
    ├── 1.bukti_serving.png
    ├── 2.prometheus.yml
    ├── 3.prometheus_exporter.py
    ├── 4.bukti monitoring Prometheus/
    ├── 5.bukti monitoring Grafana/
    ├── 6.bukti alerting Grafana/
    └── 7.inference.py
```

## 🚀 Teknologi yang Digunakan

- **ML Framework:** Scikit-learn, MLflow
- **CI/CD:** GitHub Actions
- **Containerization:** Docker
- **Monitoring:** Prometheus, Grafana
- **Deployment:** MLflow Model Serving

## 📦 Instalasi & Setup

### 1. Clone Repository

```bash
git clone https://github.com/ainifadillahn/Eksperimen_SML_Nur-Aini-Fadillah
cd Eksperimen_SML_Nur-Aini-Fadillah
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Serve Model

```bash
cd Membangun_model
mlflow models serve -m "mlruns/.../artifacts" -h 0.0.0.0 -p 5001 --no-conda
```

## 🔄 CI/CD Pipeline

Workflow otomatis di-trigger saat push ke `main`:

1. **Training:** Model dilatih ulang dengan MLflow
2. **Tracking:** Metrics & artifacts disimpan
3. **Docker Build:** Image dibuat dengan Dockerfile
4. **Push:** Image di-push ke Docker Hub

**File Workflow:** `.github/workflows/main.yml`

## 📊 Monitoring & Logging

### Prometheus Metrics

- `model_prediction_total`: Total prediksi
- `model_prediction_high_risk`: Jumlah prediksi high risk
- `model_latency_seconds`: Latency model

### Grafana Alerting Rules

- High risk machines > threshold
- Model latency > 2 seconds
- Error rate > 5%

**Setup Monitoring:**

```bash
cd "Monitoring dan Logging"
python 3.prometheus_exporter.py
```

## 🐳 Docker

### Pull dan Jalankan Model

```bash
docker pull ainifadillahn/ai4i2020-model:latest
docker run -p 5001:8080 ainifadillahn/ai4i2020-model:latest
```

## 📞 API Endpoint

### Health Check

```bash
curl http://localhost:5001/health
```

### Prediction

```bash
curl -X POST http://localhost:5001/invocations \
  -H "Content-Type: application/json" \
  -d '{
    "dataframe_split": {
      "columns": ["Type", "Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]"],
      "data": [[2, 298.1, 308.6, 1551, 42.8, 50]]
    }
  }'
```

## 👤 Author

**Nur Aini Fadillah**

- GitHub: [@ainifadillahn](https://github.com/ainifadillahn)
- Docker Hub: [ainifadillahn/ai4i2020-model](https://hub.docker.com/r/ainifadillahn/ai4i2020-model)

## 📄 License

This project is created for educational purposes as part of Machine Learning Operations course **Asah Dicoding**.