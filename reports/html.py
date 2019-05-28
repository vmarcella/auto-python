from datetime import datetime

from jinja2 import Template


def main() -> None:
    """
        Generate an html based report
    """
    movie_data = {
        "date": datetime.now(),
        "movies": ["Casablanca", "The sound of music", "Vertigo"],
        "total_minutes": 404,
    }
    # Obtain the template from the html file
    with open("jinja_template.html") as file:
        template = Template(file.read())

    # Render the template using our movie data. Dictionary
    # Keys match the template fields within the html file
    with open("report.html", "w") as file:
        file.write(template.render(movie_data))


if __name__ == "__main__":
    main()
