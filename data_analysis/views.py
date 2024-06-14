# myapp/views.py
from django.shortcuts import render, redirect
from .forms import UploadFileForm
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings

import matplotlib
matplotlib.use('Agg')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)
            # Save the DataFrame to session
            request.session['csv_data'] = df.to_dict()
            # Show the option to display first 5 records
            return render(request, 'display_option.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def show_first_five_records(request):
    # Retrieve the DataFrame from session
    csv_data = request.session.get('csv_data', None)
    if csv_data:
        df = pd.DataFrame(csv_data)
        first_five_records = df.head(5).to_html()
        return render(request, 'display_records.html', {'records': first_five_records})
    return render(request, 'error.html', {'message': 'No data available'})

def show_summary_statistics(request):
    # Retrieve the DataFrame from session
    csv_data = request.session.get('csv_data', None)
    if csv_data:
        df = pd.DataFrame(csv_data)
        summary = df.describe().to_html()

        # Calculate missing values
        missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()

        return render(request, 'summary.html', {'summary': summary, 'missing_values': missing_values})
    return render(request, 'error.html', {'message': 'No data available'})

def handle_missing_values(request):
    # Retrieve the DataFrame from session
    csv_data = request.session.get('csv_data', None)
    if csv_data:
        df = pd.DataFrame(csv_data)
        
        # Example: Fill missing values with the column mean
        df.fillna(df.mean(), inplace=True)
        
        # Update the session with the modified DataFrame
        request.session['csv_data'] = df.to_dict()
        
        return redirect('show_summary_statistics')
    return render(request, 'error.html', {'message': 'No data available'})


def generate_histograms(request):
    # Retrieve the DataFrame from session
    csv_data = request.session.get('csv_data', None)
    if csv_data:
        df = pd.DataFrame(csv_data)
        numerical_columns = df.select_dtypes(include=['number']).columns

        # Create a directory for storing plots if it doesn't exist
        plots_dir = os.path.join(settings.MEDIA_ROOT, 'plots')
        if not os.path.exists(plots_dir):
            os.makedirs(plots_dir)
        
        # Generate histograms for numerical columns
        plot_paths = []
        for column in numerical_columns:
            plt.figure()
            sns.histplot(df[column].dropna(), kde=True)
            plot_path = os.path.join(plots_dir, f'{column}_histogram.png')
            plt.savefig(plot_path)
            plt.close()
            plot_paths.append(os.path.join(settings.MEDIA_URL, 'plots', f'{column}_histogram.png'))
        
        return render(request, 'histogram.html', {'plot_paths': plot_paths})
    return render(request, 'error.html', {'message': 'No data available'})


def generate_scatter_plots(request):
    # Retrieve the DataFrame from session
    csv_data = request.session.get('csv_data', None)
    if csv_data:
        df = pd.DataFrame(csv_data)
        numerical_columns = df.select_dtypes(include=['number']).columns

        # Create a directory for storing plots if it doesn't exist
        plots_dir = os.path.join(settings.MEDIA_ROOT, 'plots')
        if not os.path.exists(plots_dir):
            os.makedirs(plots_dir)

        # Generate scatter plots for numerical columns
        plot_paths = []
        for i in range(len(numerical_columns)):
            for j in range(i + 1, len(numerical_columns)):
                plt.figure()
                sns.scatterplot(x=df[numerical_columns[i]], y=df[numerical_columns[j]])
                plot_path = os.path.join(plots_dir, f'{numerical_columns[i]}_vs_{numerical_columns[j]}_scatter.png')
                plt.savefig(plot_path)
                plt.close()
                plot_paths.append(os.path.join(settings.MEDIA_URL, 'plots', f'{numerical_columns[i]}_vs_{numerical_columns[j]}_scatter.png'))

        return render(request, 'scatter_plot.html', {'plot_paths': plot_paths})
    return render(request, 'error.html', {'message': 'No data available'})


def generate_heatmaps(request):
    
    csv_data = request.session.get('csv_data', None)
    if csv_data:
        df = pd.DataFrame(csv_data)
        numerical_columns = df.select_dtypes(include=['number'])

        # Create a directory for storing plots if it doesn't exist
        plots_dir = os.path.join(settings.MEDIA_ROOT, 'plots')
        if not os.path.exists(plots_dir):
            os.makedirs(plots_dir)

        # Generate heatmap for the correlation matrix of numerical columns
        plt.figure()
        sns.heatmap(numerical_columns.corr(), annot=True, cmap='coolwarm')
        plot_path = os.path.join(plots_dir, 'heatmap.png')
        plt.savefig(plot_path)
        plt.close()

        plot_paths = [os.path.join(settings.MEDIA_URL, 'plots', 'heatmap.png')]

        return render(request, 'heatmap.html', {'plot_paths': plot_paths})
    return render(request, 'error.html', {'message': 'No data available'})


def generate_box_plots(request):
    # Retrieve the DataFrame from session
    csv_data = request.session.get('csv_data', None)
    if csv_data:
        df = pd.DataFrame(csv_data)
        numerical_columns = df.select_dtypes(include=['number']).columns

        # Create a directory for storing plots if it doesn't exist
        plots_dir = os.path.join(settings.MEDIA_ROOT, 'plots')
        if not os.path.exists(plots_dir):
            os.makedirs(plots_dir)

        # Generate box plots for numerical columns
        plot_paths = []
        for column in numerical_columns:
            plt.figure()
            sns.boxplot(x=df[column])
            plot_path = os.path.join(plots_dir, f'{column}_boxplot.png')
            plt.savefig(plot_path)
            plt.close()
            plot_paths.append(os.path.join(settings.MEDIA_URL, 'plots', f'{column}_boxplot.png'))

        return render(request, 'boxplot.html', {'plot_paths': plot_paths})
    return render(request, 'error.html', {'message': 'No data available'})