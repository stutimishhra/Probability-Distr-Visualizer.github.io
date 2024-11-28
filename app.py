from flask import Flask, render_template, request, url_for
import matplotlib.pyplot as plt
import os

# Import functions for PDFs
from pdf_functions.binomial import binomial_pdf
from pdf_functions.poisson import poisson_pdf
from pdf_functions.geometric import geometric_pdf
from pdf_functions.negative_binomial import negative_binomial_pdf
from pdf_functions.hypergeometric import hypergeometric_pdf
from pdf_functions.normal import normal_pdf
from pdf_functions.exponential import exponential_pdf
from pdf_functions.uniform import uniform_pdf
from pdf_functions.gamma import gamma_pdf
from pdf_functions.beta import beta_pdf

app = Flask(__name__)

# Helper to save and serve plot with a specific filename and return data points for table display
def save_plot_with_data(title, x_data, y_data):
    filename = f"{title}.png"
    static_path = os.path.join('static', filename)
    plt.savefig(static_path)
    plt.close()
    data_points = list(zip(x_data, y_data))
    return url_for('static', filename=filename), data_points

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    pdf_type = request.form.get('pdfType')
    plot_url = None
    data_points = []

    # Handle each PDF type
    if pdf_type == 'binomial':
        x_data, y_data = binomial_pdf(n=10, p=0.5)
        plot_url, data_points = save_plot_with_data("binomial_distribution", x_data, y_data)
    elif pdf_type == 'poisson':
        x_data, y_data = poisson_pdf(lam=5)
        plot_url, data_points = save_plot_with_data("poisson_distribution", x_data, y_data)
    elif pdf_type == 'geometric':
        x_data, y_data = geometric_pdf(p=0.5)
        plot_url, data_points = save_plot_with_data("geometric_distribution", x_data, y_data)
    elif pdf_type == 'negative_binomial':
        x_data, y_data = negative_binomial_pdf(r=5, p=0.5)
        plot_url, data_points = save_plot_with_data("negative_binomial_distribution", x_data, y_data)
    elif pdf_type == 'hypergeometric':
        x_data, y_data = hypergeometric_pdf(M=50, n=10, N=20)
        plot_url, data_points = save_plot_with_data("hypergeometric_distribution", x_data, y_data)
    elif pdf_type == 'normal':
        x_data, y_data = normal_pdf(mu=0, sigma=1)
        plot_url, data_points = save_plot_with_data("normal_distribution", x_data, y_data)
    elif pdf_type == 'exponential':
        x_data, y_data = exponential_pdf(lam=1)
        plot_url, data_points = save_plot_with_data("exponential_distribution", x_data, y_data)
    elif pdf_type == 'uniform':
        x_data, y_data = uniform_pdf(a=0, b=10)
        plot_url, data_points = save_plot_with_data("uniform_distribution", x_data, y_data)
    elif pdf_type == 'gamma':
        x_data, y_data = gamma_pdf(shape=2, scale=2)
        plot_url, data_points = save_plot_with_data("gamma_distribution", x_data, y_data)
    elif pdf_type == 'beta':
        x_data, y_data = beta_pdf(a=2, b=5)
        plot_url, data_points = save_plot_with_data("beta_distribution", x_data, y_data)
    else:
        return "Invalid selection.", 400

    return render_template('index.html', plot_url=plot_url, data_points=data_points)

if __name__ == '__main__':
    app.run(debug=True)
