# Changelog

All notable changes to the MetalMind project will be documented in this file.

## [v0.2.0] - 2026-02-13

### 🚀 New Features

- **User Profiles**: Added `Profile` page allowing users to update their personal information (email, first/last name).
- **Portfolio Tracking**: Introduced `PortfolioItem` model and management interface. Users can now add/edit/delete their holdings and see total portfolio value on the dashboard.
- **Platinum & Palladium Support**: Added `platinum` (XPT) and `palladium` (XPD) to the list of tracked assets in `market/services/update_data.py`.
- **Local Timezone Display**: Implemented frontend logic to automatically convert UTC timestamps to the user's local browser time on Dashboard and Asset Detail pages.
- **Management Command**: Added `--clear` flag to `update_prices` command to wipe existing data before generating new entries.
- **Robust Validation**: Implemented `PortfolioItemForm` to handle large number inputs gracefully and prevent server errors.

### 🎨 UI/UX Improvements

- **Consistent Authentication UI**: Standardized the design of `Login` and `Sign Up` pages using a shared layout and consistent form styling.
- **Bootstrap Integration**: Applied Bootstrap classes (`form-control`, `btn-primary`, `mb-3`) to all authentication forms for a responsive and professional look.

### 🐛 Bug Fixes

- **Authentication Redirects**: Fixed 404 errors by correcting `LOGIN_URL` and `LOGIN_REDIRECT_URL` in `settings.py`.
- **Template Filters**: Resolved `TemplateSyntaxError` by implementing a custom `currency` filter to replace the problematic `floatform` usage in templates.
- **Import Errors**: Fixed a `NameError` crash by restoring missing imports in `accounts/forms.py`.

### 📚 Documentation

- **README.md**: Created comprehensive project documentation with installation steps, features list, and usage guide.
- **CHANGELOG.md**: Started tracking project updates in this file.

---

## [v0.1.0] - Initial Release

- Basic Django project structure with `accounts` and `market` apps.
- Core models: `Asset`, `PriceSnapshot`, `PriceCandle`.
- Basic Dashboardview and Asset Detail view.
- Initial mock data generation.
