def find_drugs_in_title(title, drugs_list):
    """
    Finds all the drugs in the title and returns them as a list
    """
    drugs_found = []

    title_words = title.split()
    for word in title_words:
        if word in drugs_list:
            drugs_found.append(word)
    
    return list(set(drugs_found))