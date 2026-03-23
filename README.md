# 🔐 Diffie-Hellman Key Exchange Simulator

A web-based interactive simulator that demonstrates how two users can securely exchange a secret key over an insecure channel using the Diffie-Hellman algorithm.

---

## 📌 Overview

This project visualizes the **Diffie-Hellman Key Exchange**, a fundamental concept in cryptography used in real-world secure communication protocols.

It allows users to:

* Input custom parameters
* Generate public keys
* Compute a shared secret key
* Understand the step-by-step process interactively

---

## 🧠 How It Works

1. Two users agree on public values:

   * Prime number `p`
   * Generator `g`

2. Each user selects a private key:

   * User A → `a`
   * User B → `b`

3. Public keys are generated:

   * A = g^a mod p
   * B = g^b mod p

4. Shared secret key is computed:

   * Key = B^a mod p = A^b mod p

Even though public values are exchanged openly, the private keys remain secure.

---

## 🚀 Features

* 🔹 Interactive UI using Streamlit
* 🔹 Real-time key generation
* 🔹 Clean modular architecture
* 🔹 Beginner-friendly visualization of cryptographic concepts
* 🔹 Input validation support (optional utils module)

---

## 🏗️ Project Structure

```
diffie-hellman-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── core/
│   └── diffie_hellman.py
│
├── utils/
│   └── helpers.py
│
├── assets/
│   └── dh-diagram.png
│
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/diffie-hellman-app.git
cd diffie-hellman-app
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🌐 Usage

* Enter values for:

  * Prime number `p`
  * Generator `g`
  * Private keys `a` and `b`

* Click **Generate Keys**

* View:

  * Public keys
  * Shared secret key

---

## 🔐 Security Concept

This project is based on the **Discrete Logarithm Problem**, which makes it computationally difficult to derive private keys from public values, ensuring secure communication.

---

## 💻 Tech Stack

* Python 🐍
* Streamlit 🎨

---

## 📈 Future Enhancements

* 🔥 Man-in-the-Middle (MITM) attack simulation
* 🔥 Encryption using generated key
* 🔥 Visualization of key exchange process
* 🔥 Deployment on Streamlit Cloud

---

