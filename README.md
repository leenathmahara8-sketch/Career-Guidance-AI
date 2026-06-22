# Random Forest Model Training

## Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Model Training Script
```bash
python random_forest_model.py
```

## What the Script Does

1. **Loads Dataset**: Reads the Excel file `career data_ set.csv (1).xlsx`
2. **Explores Data**: Shows dataset shape, info, and missing values
3. **Preprocessing**:
   - Handles missing values (median for numeric, mode for categorical)
   - Encodes categorical variables using LabelEncoder
4. **Splits Data**: 80% training, 20% testing
5. **Trains Model**: Random Forest with 100 trees
6. **Evaluates**: Shows accuracy, classification report, and confusion matrix
7. **Visualizes**: Creates feature importance and confusion matrix plots

## Output

- **Console Output**: Accuracy, classification metrics
- **feature_importance.png**: Top 10 most important features
- **confusion_matrix.png**: Confusion matrix visualization

## Model Parameters (Customizable)

- `n_estimators`: Number of trees (default: 100)
- `max_depth`: Max tree depth (default: 15)
- `min_samples_split`: Min samples to split (default: 5)
- `min_samples_leaf`: Min samples at leaf (default: 2)
- `test_size`: Test set percentage (default: 0.2)

## Results Interpretation

- **Accuracy**: Percentage of correct predictions
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of precision and recall
