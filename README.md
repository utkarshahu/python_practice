
---

# 🧠 Python Virtual Environment + Conda Cheat Sheet

## 📦 1. Create Environment

```bash
conda create --name machineLearning
```

👉 Creates a new environment named `machineLearning`

---

## ▶️ 2. Activate Environment

```bash
conda activate machineLearning
```

---

## ⏹️ 3. Deactivate Environment

```bash
conda deactivate
```

---

## ❌ 4. Delete Environment

```bash
conda remove --name machineLearning --all
```

---

## 📋 5. List All Environments

```bash
conda env list
```

or

```bash
conda info --envs
```

---

## 📚 6. Install Libraries

### Install from default channel:

```bash
conda install numpy
```

### Install from specific channel:

```bash
conda install -c anaconda jupyter
```

---

## 🧹 7. Remove a Library

```bash
conda remove numpy
```

---

## 🔄 8. Update a Library

```bash
conda update numpy
```

---

## 🔼 9. Update Conda

```bash
conda update -n base -c defaults conda
```

---

## 📦 10. Install Multiple Packages

```bash
conda install numpy pandas matplotlib
```

---

## 📤 11. Export Environment (Backup)

```bash
conda env export > environment.yml
```

---

## 📥 12. Create Environment from File

```bash
conda env create -f environment.yml
```

---

## 🧪 13. Run Jupyter Notebook

```bash
jupyter notebook
```

👉 Opens browser at:

```
http://localhost:8888
```

---

## ⚠️ 14. Common Issue (From Your Log)

### ❌ Error:

```
Kernel does not exist
```

### ✅ Fix:

* Restart Jupyter
* Or install kernel:

```bash
conda install ipykernel
python -m ipykernel install --user --name machineLearning
```

---

## 🔍 15. Check Installed Packages

```bash
conda list
```

---

## 🧱 16. Create Environment with Python Version

```bash
conda create -n myenv python=3.10
```

---

## ⚡ 17. Quick Workflow (Your Case)

```bash
conda create --name machineLearning
conda activate machineLearning
conda install -c anaconda jupyter
conda install numpy
jupyter notebook
```

---

## 🧠 Pro Tips

* Always activate env before installing packages
* Use separate env for each project
* Keep base env clean

---
