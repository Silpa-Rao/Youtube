#  Global YouTube Statistics

This project looks at YouTube data from around the world. It helps us understand what types of videos are popular, which countries get the most views, and what makes a video successful.

## What's in the Dataset?

The file `Global YouTube Statistics 1.csv` has information like:
- Video title and channel name
- Country the video is from
- Video category (like Music, Education, etc.)
- Number of subscribers
- Number of views, likes, and comments
- Year the video was published

##  What This Project Does

- Cleans the `Global YouTube Statistics 1.csv` dataset by handling missing values, fixing messy entries, and standardizing formats for analysis.
- Predicts `lowest_yearly_earnings` of YouTube channels using Random Forest and XGBoost models, with hyperparameter tuning via GridSearchCV to optimize performance.
- Identifies top-performing YouTube channels based on predicted earnings and channel metrics like subscribers and views.
- Analyzes trends in the data: - Determines which countries have the most views and likes to understand global engagement patterns.
- Checks which video categories (e.g., Music, Education) are the most popular based on views and subscriber counts.
- Explores how the year of video uploads impacts channel success, revealing temporal trends in YouTube growth.

##  File in This Project

- `Global YouTube Statistics 1.csv` — This is the main file with all the YouTube data.

## How to Use It

- Clone the repository: ```bash git clone https://github.com/your-username/your-repo-name.git cd your-repo-name ```
- Install required packages: ```bash pip install numpy pandas scikit-learn xgboost ```
- Ensure the dataset `Global YouTube Statistics 1.csv` is in the project directory.
- Run the script to train models and view results: ```bash python main.py ```
- Check the output for: - Best Random Forest and XGBoost parameters - Model performance (R², MSE, MAPE) - Top feature importances
