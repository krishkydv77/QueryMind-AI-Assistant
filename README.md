#  QueryMind AI

### Intelligent Natural Language-to-SQL Assistant

**QueryMind AI** is an intelligent Natural Language-to-SQL assistant powered by **Google Gemini** that enables users to interact with MySQL databases using **English, Hindi, or Hinglish**.

It understands natural-language questions, converts them into **optimized MySQL queries**, executes the queries against the database, and presents the results through a clean and interactive **Streamlit interface**.

> **Ask naturally. Generate optimized SQL. Explore your data.**


## Key Features

*  **AI-Powered SQL Generation** using Google Gemini
*  Supports **English, Hindi, and Hinglish**
*  Converts natural-language questions into **optimized MySQL queries**
*  Direct **MySQL database integration**
*  Interactive query-result visualization using Pandas and Streamlit
*  Simple natural-language database interaction
*  Professional Streamlit-based user interface
*  Environment-based configuration for API and database credentials
*  User-friendly messages when requested data is unavailable


##  How It Works

QueryMind AI follows a simple Natural Language-to-SQL workflow:

```text
                    User Question
                         │
                         ▼
              English / Hindi / Hinglish
                         │
                         ▼
                  Google Gemini
                         │
                         ▼
              SQL Query Generation
                         │
                         ▼
             Optimized MySQL Query
                         │
                         ▼
                  MySQL Database
                         │
                         ▼
                Query Execution
                         │
                         ▼
                  Pandas DataFrame
                         │
                         ▼
              Streamlit Result Display
```



## 🛠️ Technology Stack

| Technology                 | Purpose                            |
| -------------------------- | ---------------------------------- |
| **Python**                 | Core application development       |
| **Google Gemini**          | Natural Language-to-SQL generation |
| **Streamlit**              | Interactive web interface          |
| **MySQL**                  | Relational database                |
| **Pandas**                 | Query result processing            |
| **mysql-connector-python** | MySQL database connectivity        |
| **python-dotenv**          | Environment variable management    |


##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/querymind-ai.git
```

Navigate into the project:

```bash
cd querymind-ai
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

#### Windows

```bash
venv\Scripts\activate
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```



##  Environment Configuration

Create a `.env` file in the project root directory.

```env
GOOGLE_API_KEY=your_google_gemini_api_key

DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
```



##  Project Objective

The main objective of QueryMind AI is to simplify database interaction through natural language.

The project demonstrates how **Generative AI can be integrated with traditional relational databases** to create an intelligent Natural Language-to-SQL interface.

It bridges the gap between:

```text
Natural Language
        ↓
Generative AI
        ↓
SQL
        ↓
Relational Database
        ↓
Structured Results
```

</div>
