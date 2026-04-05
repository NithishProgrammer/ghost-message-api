
# 👻 Ghost Message API

A high-performance, "Burn-on-Read" messaging service built with **FastAPI**. Designed for sending sensitive information that needs to vanish the moment it is viewed.

-----

## ✨ Features

  * **In-Memory Storage:** Messages live in system RAM. No database footprint, no logs, no permanent trace.
  * **Instant Destruction:** Implements a strict "Read-Once" policy using Python's list-removal logic.
  * **Secure IDs:** Generates unique `UUID` strings for every secret to prevent URL guessing or brute-force attacks.
  * **Auto-Generated Docs:** Full interactive API documentation available out-of-the-box via Swagger UI.

## 🚀 Quick Start

### 1\. Prerequisites

  * Python 3.8+
  * FastAPI
  * Uvicorn

### 2\. Installation

```bash
# Clone the repository
git clone https://github.com/NithishProgrammer/ghost-msg-api.git

# Change into the directory
cd ghost-msg-api

# Install dependencies
pip install fastapi uvicorn
```

### 3\. Run the Server

```bash
uvicorn main:app --reload
```

The API will be live at `http://127.0.0.1:8000`.

-----

## 🛠 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/post` | Create a secret. Returns a unique `mid`. |
| `GET` | `/secret/{m_id}` | Retrieve the secret and **burn** it immediately. |
| `GET` | `/docs` | Access the interactive Swagger UI. |

-----

## 🧠 The Logic Behind the "Burn"

This project demonstrates core backend engineering concepts:

1.  **Data Modeling:** Uses `Pydantic` to ensure incoming messages are strictly strings.
2.  **State Management:** Handles a global list of dictionaries to track active secrets during the server session.
3.  **Linear Search & Destroy:** \* The API iterates through the `messages` list to find a matching `mid`.
      * Once found, it captures the message, performs a `.remove()`, and returns the data.
      * This ensures that any subsequent request to the same ID returns a `404` style alert.

-----

## 🧪 Testing with Swagger

1.  Navigate to `http://127.0.0.1:8000/docs`.
2.  Use the **POST** endpoint to create a message (e.g., `{"message": "Top Secret"}`).
3.  Copy the `mid` from the response.
4.  Use the **GET** endpoint with that `mid` to see your secret.
5.  Try to refresh or use the **GET** endpoint again—you will receive the "Already Burned" alert\!

-----

## 🤝 Contributing

Developed by **[NithishProgrammer](https://github.com/NithishProgrammer)**.

Feel free to fork this, open issues, or suggest new "destruction" methods like:

  * **Timed Expiry:** Automatically delete messages after 60 seconds.
  * **Encryption:** Encrypting the strings before they hit the list.

## 📝 License

This project is licensed under the MIT License.

-----

