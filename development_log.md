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