# My Solution to the Xelix Backend Technical Challenge to be done in a hour (took me 2)

Xelix requires a solution to extract information and identify problems with supplier invoices. A developer has started by creating a simple Django application to store and display the data. The application has a management command to generate fake demo data. 

## Environment Setup

The project dependencies are listed in the requirements.txt file. You may like to create yourself a virtual environment from which to run the project. 

You will need to initialize the database and run a script to populate it with demo data by running the following commands:

```bash
python manage.py migrate
python manage.py demo_data
```

Run the project with:

```bash
python manage.py runserver
```

Optionally, you can create an admin user for use with the Django admin:

```bash
python manage.py createsuperuser
```

## Tasks

For the following tasks, if you feel that additional packages would assist you or improve your answers feel free to install them.
If at any point you have a question not answered during the introduction to the interview, make an informed assumption, and we can discuss it during the debrief.
Both tasks have an equal weight.
If you think you're finished with both tasks, you may add any "nice-to-haves" to either of them.

### Task 1 - Invoice Length Pattern

This task focuses on your general Python skills.
In the file analyse.py, a skeleton program has been written; you may run this command with:

```bash
python analyse.py
```

Update the script to calculate the frequency of invoice number lengths for each supplier, outputting the count of invoices with a given invoice number length and a percentage of the total for that supplier. The result of this analysis should be printed to the terminal.

For example, given the input in this table:

| Supplier Reference | Invoice Number |
|--------------------|----------------|
| ALP1               | AB012          |
| ALP1               | AB015          |
| ALP1               | AB020          |
| ALP1               | CF3            | 
| BET1               | JJ088          | 
| BET1               | JJ199          |

The output would be:

| Supplier Reference | Invoice Number Length | Frequency | Percentage |
|--------------------|-----------------------|-----------|------------|
| ALP1               | 5                     | 3         | 75%        |
| ALP1               | 3                     | 1         | 25%        |
| BET1               | 5                     | 2         | 100%       |


### Task 2 - Supplier Information

This task focuses on your Django skills, and it's separate from the previous task.

#### Part 1

Currently, a supplier reference is stored for each invoice. The business would now like to store each supplier's company name and government issued company number in the database.

Make the required changes to store this information.

#### Part 2

Create a view to list the invoices. Display all the invoice fields including the supplier information you added in Part 1. This can be either a Django template view, or a Django REST Framework view.

#### Part 3

Extend the view you have written to accept a URL parameter that filters the invoice list by the supplier reference.
