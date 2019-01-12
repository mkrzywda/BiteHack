import csv
import movie

def get_principals( Movie, base):
    action = False
    principals_list = [[],[],[]] #directorID, writerID, actor/acressID
    with open(base) as principals:
        principals = csv.reader(principals, delimiter='\t')
        for row in principals:
            if row[0] == Movie.ID:
                if row[3] == 'writer':
                    principals_list[1].append(row[2])
                    action = True
                elif row[3] == 'actor' or row[3] == 'actress':
                    action = True
                    principals_list[2].append(row[2])
                elif row[3] == 'director':
                    principals_list[0].append(row[2])
                    action = True
    if action == True: return principals_list
    else: return False

def set_principals_name(principalIDs, base, Movie):
    quantity_of_principals = sum(len(x) for x in principalIDs)
    counter = 0
    with open(base) as principals:
        principals = csv.reader(principals, delimiter='\t')
        for row in principals:
            if row[0] in principalIDs[0]:
                Movie.direction.append(row[1])
                counter+=1
            if row[0] in principalIDs[1]:
                Movie.scenario.append(row[1])
                counter+=1
            if row[0] in principalIDs[2]:
                Movie.actors.append(row[1])
                counter+=1
            if counter == quantity_of_principals: return Movie
    return Movie

test_movie = movie.Movie()
test_movie.ID = 'tt3315342'
test_principal_list = get_principals( test_movie, '../data/principals_data.tsv')


print(set_principals_name(test_principal_list, '../data/basic_personal_data.tsv', test_movie).actors)
