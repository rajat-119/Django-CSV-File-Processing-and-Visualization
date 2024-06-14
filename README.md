# Django-CSV-File-Processing-and-Visualization

This Django project allows users to upload a CSV file, display the first five records, show summary statistics, handle missing values, and generate various plots (histograms, scatter plots, heatmaps, and box plots). The plots are generated using Matplotlib and Seaborn.

## Features

- Upload CSV files through a web interface.
- Display the first five records of the uploaded CSV.
- Show summary statistics (mean, median, standard deviation) for numerical columns.
- Identify and display missing values in the dataset.
- Handle missing values by filling them with the column mean.
- Generate and display histograms for numerical columns.
- Generate and display scatter plots for pairs of numerical columns.
- Generate and display heatmaps for the correlation matrix of numerical columns.
- Generate and display box plots for numerical columns.

## Prerequisites

- Python 3.x
- Django
- Pandas
- Matplotlib
- Seaborn
- 
## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/django-csv-visualization.git
cd django-csv-visualization
```

2. Create a virtual environment and activate it:
```python -m venv venv```
`venv\Scripts\activate`

4. Install the required packages:
pip install -r requirements.txt

5. Apply the migrations:
python manage.py migrate

6. Run the development server:
python manage.py runserver

Open your web browser and go to 'http://127.0.0.1:8000/data_analysis/'.

## Usage:
Upload CSV File: Upload a CSV file through the upload page.
- dummy .csv file give by the name of test.csv .

## Select Option: After uploading, choose from various options:
- Show First 5 Records
- Show Summary Statistics
- Handle Missing Values
- Generate Histogram
- Generate Scatter Plot
- Generate Heatmap
- Generate Box Plot
  

## Project Structure:
- The name of our main Django project is fileupload.
- The app we created for the mian functionality is by the name data_analysis.
- data_analysis/: Contains the Django app files.
- data_analysis/views.py: contians all the logics and main code.
- data_analysis/templates/: Contains the HTML templates for the application.
- views.py: Contains the views for handling file uploads, displaying records, summary statistics, handling missing values, and generating plots.
- urls.py: Contains the URL patterns for the application.
- forms.py: Contains the form for file uploads.


