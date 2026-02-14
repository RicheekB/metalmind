# 🛡️ MetalMind

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

**MetalMind** is a robust Django-based asset tracking application designed for monitoring precious metal prices. It features a real-time dashboard, detailed asset analytics, and dynamic mock data generation, all wrapped in a clean, responsive Bootstrap UI.

## 🚀 Features

- **🔐 Secure Authentication**: Full user signup, login, and logout flows with form validation.
- **📊 Interactive Dashboard**: View real-time prices, daily change percentages, and status indicators for Gold, Silver, Platinum, and Palladium.
- **📈 Asset Analytics**: Detailed views for individual assets showing historical data and trends.
- **🌍 Local Timezone Support**: Automatically detects and renders timestamps in your local timezone.
- **⚡ Dynamic Data**: Integrated mock data generator to simulate market movements for testing.

---

## 🛠️ Built With

- **Framework**: [Django](https://www.djangoproject.com/)
- **Frontend**: [Bootstrap 5](https://getbootstrap.com/), JavaScript
- **Database**: SQLite (default), extensible to PostgreSQL/MySQL

---

## 🏁 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/metalmind.git
    cd metalmind
    ```

2.  **Create and activate a virtual environment**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install django
    ```

4.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Generate Mock Data**
    Populate the database with initial price data:
    ```bash
    python manage.py update_prices --days 30 --clear
    ```

6.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/` in your browser.

---

## 🕹️ Usage

### Management Commands

MetalMind includes a custom management command to simulate market data.

**Update Prices**
Generates mock price history for tracking assets.

```bash
python manage.py update_prices [options]
```

**Options:**
- `--days <int>`: Number of days of history to generate (Default: 5).
- `--clear`: **Destructive**. Wipes all existing price data before generating new entries.

**Example:**
```bash
# Clear old data and generate 3 months of history
python manage.py update_prices --days 90 --clear
```

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
