#  Global YouTube Statistics

This project looks at YouTube data from around the world. It helps us understand what types of videos are popular, which countries get the most views, and what makes a video successful.

## What's in the Dataset?

The file `Global YouTube Statistics.csv` has information like:
- Video title and channel name
- Country the video is from
- Video category (like Music, Education, etc.)
- Number of subscribers
- Number of views, likes, and comments
- Year the video was published

##  What This Project Does

- Cleans the `Global YouTube Statistics.csv` dataset by handling missing values, fixing messy entries, and standardizing formats for analysis.
- Predicts `lowest_yearly_earnings` of YouTube channels using Random Forest and XGBoost models, with hyperparameter tuning via GridSearchCV to optimize performance.
- Identifies top-performing YouTube channels based on predicted earnings and channel metrics like subscribers and views.
- Analyzes trends in the data: - Determines which countries have the most views and likes to understand global engagement patterns.
- Checks which video categories (e.g., Music, Education) are the most popular based on views and subscriber counts.
- Explores how the year of video uploads impacts channel success, revealing temporal trends in YouTube growth.

##  File in This Project

- `Global YouTube Statistics.csv` — This is the main file with all the YouTube data.
  
## 🔧 DataOps

### ✅ Step 1: Data Ingestion
- Loaded CSV with encoding
- Trimmed and standardized column names

### ✅ Step 2: Data Cleaning
- Removed currency symbols, commas, and invalid placeholders (`N/A`, `-`)
- Converted numeric-like strings to `float` using `pd.to_numeric`
- Dropped rows with missing critical numeric fields

### ✅ Step 3: Feature Engineering
- **Log-transformed** skewed numeric features (e.g., `subscribers`, `video_views`)
- One-hot encoded categorical variables like `country`, `channel_type`, and `category`
- Added `rating_count` as a proxy for popularity

### ✅ Step 4: Modeling Preparation
- Defined `X` (features) and `y` (target: `lowest_yearly_earnings`)
- Scaled numeric data and encoded categorical data using `ColumnTransformer`

## 🔧 ModelOps

### ✅ Step 1: Train Model
- We used RandomForest and XGBooster regressors.
- Found xgboost is providing more accuracy.

### ✅ Step 2: Tracking Model
- Using ML flow we are tracking the model versioning.
- We tracked 2 models(RF & XGB) with 3 different parameters and found XGBoost is giving more accuracy. 
  
## 🧠 Project Goals
- Predict annual earnings of YouTube creators
- Understand key drivers behind income potential
- Build a scalable, clean, and interpretable dataset for ML

## How to Use It

- Clone the repository: ```bash git clone https://github.com/your-username/your-repo-name.git cd your-repo-name ```
- Install required packages: ```bash pip install numpy pandas scikit-learn xgboost mlflow fastapi uvicorn streamlit ```
- Ensure the dataset `Global YouTube Statistics.csv` is in the project directory.
- Run the script to train models and view results: ```bash python main.py ```
- Check the output for: - Best Random Forest and XGBoost parameters - Model performance (R², MSE, MAPE) - Top feature importances
- Open bash in venv folder and type 'Scripts/Activate.psl'
- To view the FastAPI Run cmd 'uvicorn main:app --reload' and Open http://127.0.0.1:8000/docs in your browser.
- Json format
  ```json
{
"data": {
"Gross tertiary education enrollment (%)": 68.5,
"uploads": 120,
"video views": 12345678,
"video_views_rank": 450,
"Population": 9800000,
"Urban_population": 7200000,
"subscribers": 256000,
"subscribers_for_last_30_days": 4800,
"country_rank": 42,
"channel_type_rank": 5,
"video_views_for_the_last_30_days": 530000,
"Unemployment rate": 5.2,
"category": "Music",
"channel_type": "Individual",
"Country": "US"
}
}
```
- To view the streamlit user interface Run cmd 'streamlit run app.py'
- Categorical columns : {category, channel_type, Country}
- Numerical columns : {Gross tertiary education enrollment (%), uploads, video views, video_views_rank, Population, Urban_population, subscribers, Subscribers_for_last_30_days,  
  country_rank, channel_type_rank, video_views_for_the_last_30_days, Unemployment rate}

👥 Contributors
Vanshika,Suraj Singh,Vivek,Supriya,Silpa
Team: BANA 7075 – Spring 2025
