import csv

def get_principals( title_ID, base, job_category):
    with open(base) as principals:
        titles = csv.reader(titles, delimiter='\t')