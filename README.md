# Odoo Legal Case Management (MVP)

Minimal Odoo 18.0 module for legal case management as per OCA MVP requirements.

## Features

- Create lawyers and clients (flags in res.partner)
- Register cases (unique sequence, minimal lifecycle)
- Calendar-based hearing planning
- Attach and view case documents (via chatter)
- One-click fixed-fee invoicing (one invoice per case)
- Simple Case Summary PDF report
- Demo data: 2 lawyers, 3 clients, 3 cases, 3 hearings

## Installation

1. Extract `legal_case_management` into your Odoo `addons_path` (e.g. `C:/MyOdooModules`)
2. Update your Odoo config (`odoo.conf`) to include your custom addons path.
3. Restart Odoo server.
4. In Odoo Apps, update the Apps list and install "Legal Case Management".

## Usage

- New menu "Legal" appears with Cases, Hearings, Lawyers, Clients.
- Everything works out-of-the-box with demo data.
- For more details, see the module documentation (if included).

## License

AGPL-3

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
