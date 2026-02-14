# MetalMind

MetalMind is a Django-based web application for tracking asset prices (Gold and Silver) with a dashboard and detailed charts.

## v0.1 Features

- User authentication (Signup/Login/Logout).
- Dashboard with latest asset prices and 24h change.
- Asset detail pages with 5-day price charts (Chart.js), trend analysis, and volatility metrics.
- Mock data generation service.
- REST API endpoints for assets and candles.

## Setup

1. **Prerequisites**: Python 3.10+ installed.

2. **Clone the repository**:

   ```bash
   git clone https://github.com/RicheekB/metalmind.git
   cd metalmind
   ```

3. **Install dependencies**:

   ```bash
   pip install django
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   Access the app at http://127.0.0.1:8000/.

## Data Updates

**Note**: v0.1 uses a **mock data provider**. Real-time data integration will be added in v0.1.1.

To generate/update mock data:

1. **Via UI**: Log in and click "Update Data" on the dashboard.
2. **Via Command Line**:
   ```bash
   python manage.py update_prices --days 5
   ```

## Development

- **Run Tests**:
  ```bash
  python manage.py test market
  ```

## License

MIT
