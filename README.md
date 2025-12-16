BVNK API Test Suite

End-to-end and integration tests for the BVNK Simulator API
Built with pytest, covering authentication, wallets, quotes, and currency conversions.

📌 Features

✅ Authentication & token handling

💼 Wallet listing and retrieval

🔁 Quote creation & acceptance

💱 Multi-currency trade flows (ETH ↔ TRX ↔ USDT)

🧪 Positive & negative test cases

📊 Balance & fee verification

⏳ Quote lifecycle & expiry checks

🧵 Parallel execution (pytest-xdist)

📄 HTML reports (pytest-html)

🐳 Docker & CI ready

🏗 Project Structure
bvnk/
├── api/
│   ├── client.py          # BVNK API client (testable)
│   ├── exceptions.py
│   └── __init__.py
│
├── helpers/
│   ├── wallets.py         # wallet mapping & balance helpers
│   ├── quotes.py          # quote helpers & polling
│   └── assertions.py     # schema & balance assertions
│
├── tests/
│   ├── test_auth.py
│   ├── test_wallets.py
│   ├── test_quotes.py
│   ├── test_trades.py     # E2E trade flows
│   └── conftest.py
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md

🐍 Requirements

Python 3.9+

pip

Internet access (tests hit BVNK simulator)

🔧 Installation
1️⃣ Clone the repository
git clone https://github.com/deep-droid/bvnk.git
cd bvnk

2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🧪 Running Tests
▶️ Run all tests
pytest
