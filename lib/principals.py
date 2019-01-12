import csv

def get_principals( title_ID, base):
    action = False
    principals_list = [[],[],[]] #directorID, writerID, actor/acressID
    with open(base) as principals:
        principals = csv.reader(principals, delimiter='\t')
        for row in principals:
            if row[0] == title_ID:
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

def get_principals_name(principalIDs, base):
    quantity_of_principals = sum(len(x) for x in principalIDs)
    print(quantity_of_principals)
    pass
    counter = 0
    result = [[],[],[]]
    with open(base) as principals:
        principals = csv.reader(principals, delimiter='\t')
        for row in principals:
            if row[0] in principalIDs[0]:
                result[0].append(row[1])
                counter+=1
            if row[0] in principalIDs[1]:
                result[1].append(row[1])
                counter+=1
            if row[0] in principalIDs[2]:
                result[2].append(row[1])
                counter+=1
            if counter == quantity_of_principals: return result
    return result


test = get_principals( 'tt0126029', 'principals_data.tsv')
print(test)
print(get_principals_name(test, 'basic_personal_data.tsv'))
