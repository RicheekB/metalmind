# System Architecture

This flowchart illustrates how the MetalMind application processes requests and manages data.

```mermaid
graph TD
    User((User/Browser))
    
    subgraph "Routing (URLs)"
        MainURLs["metalmind/urls.py"]
        AppURLs["accounts/urls.py<br>market/urls.py"]
    end
    
    subgraph "Presentation Layer (Views & Templates)"
        AuthViews["accounts/views.py<br>(Login, Signup)"]
        MarketViews["market/views.py<br>(Dashboard, Asset Detail)"]
        Templates["templates/<br>(HTML, Bootstrap, JS)"]
    end
    
    subgraph "Business Logic (Services)"
        UpdateData["market/services/update_data.py<br>(Mock Data Generator)"]
        Metrics["market/services/metrics.py<br>(Trend/Volatility Calc)"]
    end
    
    subgraph "Data Layer (Models)"
        DB[("Database<br>(SQLite)")]
        Models["market/models.py<br>(Asset, PriceSnapshot, PriceCandle)"]
    end
    
    subgraph "Management"
        Command["manage.py update_prices"]
    end

    %% Flows
    User -->|"Request (URL)"| MainURLs
    MainURLs --> AppURLs
    AppURLs -->|"Route"| AuthViews
    AppURLs -->|"Route"| MarketViews
    
    AuthViews -->|"Render"| Templates
    MarketViews -->|"Render"| Templates
    
    MarketViews -->|"Get Data"| Models
    MarketViews -->|"Calculate"| Metrics
    
    Command -->|"Run"| UpdateData
    UpdateData -->|"Save"| Models
    Models <-->|"Read/Write"| DB
    
    style User fill:#f9f,stroke:#333,stroke-width:2px
    style DB fill:#ff9,stroke:#333,stroke-width:2px
    style Command fill:#99f,stroke:#333,stroke-width:2px
```

## Description of Components

1.  **Routing**: Incoming web requests are routed via `metalmind/urls.py` to the specific app URLs (`accounts/urls.py` or `market/urls.py`).
2.  **Views**:
    *   `accounts/views.py`: Handles user registration and authentication utilizing custom forms (`accounts/forms.py`).
    *   `market/views.py`: Fetches asset data, calculates metrics using services, and prepares the context for templates.
3.  **Templates**: HTML files in `templates/` render the UI using Bootstrap. They display data passed from views (e.g., price charts, tables).
4.  **Services**:
    *   `metrics.py`: Contains pure logic for calculating trends and volatility, keeping views clean.
    *   `update_data.py`: Generates mock market data (prices, candles).
5.  **Models & Database**: `market/models.py` defines the data structure (`Asset`, `PriceSnapshot`). The application interacts with the SQLite database through these models.
6.  **Management Commands**: `update_prices` is a command-line tool that triggers `update_data.py` to populate the database, essential for the "Update Data" feature.
