# Development Log - StaySure AI

| Date | Update | Reason |
|---|---|---|
| 21 Jun 2026 | Created GitHub repository | Start version control |
| 21 Jun 2026 | Added project folders | Organise project files |
| 21 Jun 2026 | Added dataset | Prepare data for ML |
| 21 Jun 2026 | Added basic README | Briefly describe project |
| 21 Jun 2026 | Added business understanding section | To define the project goal, target column and business problem |
| 21 Jun 2026 | Loaded hotel booking demand dataset | To confirm the dataset can be read correctly in the notebook |
| 21 Jun 2026 | Completed basic data understanding | To check dataset size, columns, data types, missing values, duplicates and target distribution |
| 21 Jun 2026 | Started table-based EDA | To explore cancellation patterns without using Matplotlib or Seaborn |
| 21 Jun 2026 | Checked correlation with target | To identify numerical features that may be useful for cancellation prediction |
| 22 Jun 2026 | Continued table-based EDA | To analyse cancellation patterns without using Matplotlib or Seaborn |
| 22 Jun 2026 | Explored selected numerical features | To check how `lead_time` and `total_of_special_requests` relate to cancellation |
| 22 Jun 2026 | Explored selected categorical features | To check whether `hotel`, `deposit_type`, `market_segment` and `customer_type` may be useful after encoding |
| 22 Jun 2026 | Created feature-engineered columns for EDA | To test whether simplified booking features such as `total_nights`, `total_guests`, `has_children` and `has_special_request` show useful patterns |
| 22 Jun 2026 | Completed data cleaning | To handle missing values, remove invalid 0-guest bookings, and drop leakage columns |
| 23 Jun 2026 | Renumbered data understanding section | To make the notebook structure clearer and easier to follow |
| 23 Jun 2026 | Completed feature selection | To choose a focused set of useful features for model training |
| 23 Jun 2026 | Encoded categorical variables | To convert categorical features into numerical format using `pd.get_dummies()` |
| 23 Jun 2026 | Split dataset into training and testing sets | To prepare separate data for model training and evaluation |
| 23 Jun 2026 | Applied feature scaling | To prepare numerical features for models such as Logistic Regression |
| 23 Jun 2026 | Started model training section | To begin training classification models for hotel cancellation prediction |
| 23 Jun 2026 | Trained Logistic Regression baseline model | To create a simple baseline model for comparison with other models |
| 23 Jun 2026 | Trained Decision Tree, Random Forest and Gradient Boosting models | To compare different classification algorithms |
| 23 Jun 2026 | Evaluated models using accuracy, precision, recall and F1-score | To compare model performance on the test set |
| 23 Jun 2026 | Compared models using F1-score | To select the best model for further evaluation |