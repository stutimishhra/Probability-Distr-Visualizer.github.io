**Probability Distribution Function (PDF) Visualizer**
This project is a web application that allows users to visualize various Probability Distribution Functions (PDFs) and explore their properties. Users can select from a list of 10 different probability distributions, input specific parameters, and generate both a graph and a data table to analyze the distribution's behavior. This project is built with a Python backend and an HTML/Bootstrap frontend, ensuring responsiveness and a user-friendly interface.

**Screenshots of the project**
1- The UI
![image](https://github.com/user-attachments/assets/4746ea6f-52a6-41c2-8343-a6b3a03f177f)

2- Selection of Probability Distributions
![image](https://github.com/user-attachments/assets/6ba41fb6-bb26-4353-b37e-c88d92fb8156)

3- When selecting an option, it generates a graph
![image](https://github.com/user-attachments/assets/020bf05a-3e48-486f-9caa-f07fa9b0796f)

4- Along with a table of input and outputs
![image](https://github.com/user-attachments/assets/7f945029-082a-4fb5-a67d-922f6c479131)

5- It is fully responsive
![image](https://github.com/user-attachments/assets/015c5e67-1972-4a6d-a719-800c07bd7cb3)


**Project Features**
Graphical Visualization: Generates a line graph for each PDF based on user-defined parameters.
Data Table: Displays corresponding values in a table format below each graph for further analysis.
Responsive Design: The layout is designed to be responsive, using Bootstrap for adaptability across devices. The graph and table are shown side-by-side on larger screens and stacked vertically on smaller devices.
Interactive UI: The menu-driven interface allows users to select any of the 10 PDFs and input specific parameters.
Color Palette and Font: Styled using a modern color palette and the Quicksand font, providing a clean and professional appearance.

**Probability Distributions Available**
Binomial Distribution
Poisson Distribution
Geometric Distribution
Negative Binomial Distribution
Hypergeometric Distribution
Normal Distribution
Exponential Distribution
Uniform Distribution
Gamma Distribution
Beta Distribution

**Languages and Libraries Used**

1- Backend
Python: Main programming language used for backend calculations.
NumPy: For numerical operations and calculations related to the distributions.
Matplotlib: To generate the line graphs for each distribution.

2- Frontend
HTML: For structuring the web page.
CSS: Custom styles for visual appeal, utilizing a color palette and font for a modern look.
Bootstrap: Used for responsive design, making the web app adaptable across different screen sizes.

**Additional Libraries**
Flask: A lightweight web framework for Python used to build the backend and handle routing.
Installation and Setup

**Prerequisites**
Make sure you have the following installed:
Python 3.x
pip (Python package installer)

**Installation Steps**
1- Clone the repository:
git clone https://github.com/your-username/pdf-visualizer.git
cd pdf-visualizer

2- Install the required Python libraries:
pip install -r requirements.txt

**Running the Application**
1- Start the Flask server:
python app.py

2- Open a web browser and go to http://127.0.0.1:5000 to access the PDF Visualizer app.

**Usage Instructions**
Select a probability distribution from the dropdown menu on the homepage.
Input specific parameters for the chosen distribution.
Click the Generate Graph button to display the graph and data table for the selected distribution.

**Project Structure**

pdf-visualizer/
├── app.py                    # Main Flask application
├── requirements.txt          # Dependencies for the project
├── templates/
│   └── index.html            # HTML file for the frontend
├── static/
│   ├── styles.css            # CSS file for styling
│   └── plots/                # Folder to save generated plot images
└── pdf_functions/            # Folder containing Python files for each PDF function
    ├── binomial.py
    ├── poisson.py
    ├── geometric.py
    ├── negative_binomial.py
    ├── hypergeometric.py
    ├── normal.py
    ├── exponential.py
    ├── uniform.py
    ├── gamma.py
    └── beta.py

