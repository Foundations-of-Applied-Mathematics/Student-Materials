# solutions.py
"""Volume 3: SQL 2.
<Name>
<Class>
<Date>
"""


# Problem 1
def prob1(db_file="students.db"):
    """Query the database for the list of the names of students who have a
    'B' grade in any course. Return the list.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (list): a list of strings, each of which is a student name.
    """
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2(db_file="students.db"):
    """Query the database for all tuples of the form (Name, MajorName, Grade)
    where 'Name' is a student's name and 'Grade' is their grade in Calculus.
    Only include results for students that are actually taking Calculus, but
    be careful not to exclude students who haven't declared a major.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (list): the complete result set for the query.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3(db_file="students.db"):
    """Query the database for the list of the names of courses that have at
    least 5 students enrolled in them.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        ((list): a list of strings, each of which is a course name.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4(db_file="students.db"):
    """Query the given database for tuples of the form (MajorName, N) where N
    is the number of students in the specified major. Sort the results in
    descending order by the counts N, then in alphabetic order by MajorName.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (list): the complete result set for the query.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5(db_file="students.db"):
    """Query the database for tuples of the form (StudentName, MajorName) where
    the last name of the specified student begins with the letter C.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (list): the complete result set for the query.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6(db_file="students.db"):
    """Query the database for tuples of the form (StudentName, N, GPA) where N
    is the number of courses that the specified student is in and 'GPA' is the
    grade point average of the specified student according to the following
    point system.

        A+, A  = 4.0    B  = 3.0    C  = 2.0    D  = 1.0
            A- = 3.7    B- = 2.7    C- = 1.7    D- = 0.7
            B+ = 3.4    C+ = 2.4    D+ = 1.4

    Order the results from greatest GPA to least.

    Parameters:
        db_file (str): the name of the database to connect to.

    Returns:
        (list): the complete result set for the query.
    """
    raise NotImplementedError("Problem 6 Incomplete")
