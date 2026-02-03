<div align="center">

# 🌐 Router Manager

![Badge Development](http://img.shields.io/static/v1?label=STATUS&message=IN%20DEVELOPMENT&color=BLUE&style=for-the-badge)
<br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Networking](https://img.shields.io/badge/networking-router?style=for-the-badge&logo=cisco&logoColor=white&color=black)
![Automation](https://img.shields.io/badge/automation-script?style=for-the-badge&logo=gnu-bash&logoColor=white&color=success)

<p align="center">
  <b>Advanced tool for router automation, hotspot management, and network monitoring.</b><br>
  Focus on efficiency, stability, and ease of configuration.
</p>

</div>

---

## 💻 About the Project

**Router Manager** is a robust solution designed to automate the configuration and maintenance of network devices (such as Orbe, Teltonika, and Mikrotik).

Manual router management is error-prone and time-consuming. This project solves that by providing a streamlined interface/CLI to handle tasks like **Hotspot setup**, **remote reboots**, and **status monitoring**, ensuring high availability for your network infrastructure.

---

## ✨ Features

- **🔥 Hotspot Management**: Automate the creation and maintenance of captive portals.
- **🔄 Auto-Provisioning**: Scripts to reset and configure routers from scratch.
- **📊 Live Monitoring**: Check device health, CPU usage, and connected clients.
- **⚡ Remote Actions**: Reboot or update firmware across multiple devices instantly.
- **🛡️ Secure Connection**: Uses SSH/Telnet with secure credential handling.

---

## 🛠 Tech Stack

The project was built using:

- **Core**: [Python 3.10+](https://www.python.org/)
- **Networking**: `Netmiko` / `Paramiko` (SSH Automation).
- **Interface**: CLI (Command Line) or Web Dashboard.
- **Environment**: Virtualenv for dependency management.

---

## 🚀 How to Run

### Prerequisites
Before you begin, ensure you have met the following requirements:
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com)
- Network access to the target routers.

### 🎲 Installation

```bash
# 1. Clone this repository
$ git clone https://github.com/HenriqueLiuti5/router_manager.git

# 2. Go into the repository
$ cd router_manager

# 3. Create a virtual environment
$ python -m venv venv

# 4. Activate the virtual environment
# On Windows:
$ venv\Scripts\activate
# On Linux/Mac:
$ source venv/bin/activate

# 5. Install dependencies
$ pip install -r requirements.txt

# 6. Configure your environment variables (.env)
$ cp .env.example .env
# (Edit the .env file with your router credentials)

# 7. Run the application
$ python main.py
```

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the project.
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">
  <sub>Made by Henrique Liuti</sub>
</div>
