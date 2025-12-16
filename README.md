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

🐍 Requirements

Python 3.9+
pip



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


3️⃣ pip install -e .
Important: Always run pip install -e . whenever you add new modules in src/ so that your changes are available to tests.


🧪 Running Tests

▶️ Run all tests
pytest
