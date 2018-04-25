"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/project")
def get_project_with_title():
    """Lists the title, description, and maximum grade of a project."""

    project_title = request.args.get('project_title')

    row = hackbright.get_project_by_title(project_title)

    return render_template("project_info.html", row=row)


@app.route("/student_search")
def get_student():
    
    return render_template("student_search.html")


@app.route("/student_info")
def get_student_form():
    """Show form for searching for a student."""
    
    github = request.args.get('github')

    row_student = hackbright.get_student_by_github(github)

    row_grade = hackbright.get_grades_by_github(github)


    return render_template("student_info.html", row_student=row_student, row_grade=row_grade)


@app.route("/new_student")
def display_form():
    """Displays the form if new student"""

    return render_template("new_student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template("student-add.html",
                            github=github)



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
