
# My Careers Page

My Careers Page is a simple web application built using Flask that showcases job opportunities in various fields. This application utilizes Bootstrap for responsive design and templating to dynamically render job listings.

## Features

- **Dynamic Job Listings**: Displays a list of current job openings with details such as title, location, and salary.
- **Responsive Design**: Utilizes Bootstrap to ensure the application is mobile-friendly and visually appealing across all devices.
- **Templating**: Leverages Jinja2 templating engine to dynamically generate HTML content based on data passed from the Flask app.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Bootstrap**: A popular CSS framework for developing responsive and mobile-first websites.
- **Jinja2**: The templating engine used by Flask for rendering HTML pages.

## Project Structure

```
├── app.py                   # Main application file
└── templates                # Directory containing HTML templates
    ├── index.html          # Main landing page
    └── jobitem.html        # Template for individual job listings
```

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd my-careers-page
   ```

3. Install the required dependencies:
   ```bash
   pip install Flask
   ```

## Usage

To run the application, execute the following command:

```bash
python app.py
```

The application will start on `http://0.0.0.0:5000`. Open this URL in your web browser to view the careers page.

## Customization

- **Job Listings**: You can modify the `jobs` list in `app.py` to add, remove, or change job postings.
- **Styling**: Modify the custom CSS in `index.html` to change the appearance of the web page.
- **Templating**: Use Jinja2 syntax to customize how job listings are rendered in the `jobitem.html` template.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - For the web framework.
- [Bootstrap](https://getbootstrap.com/) - For the responsive design framework.
