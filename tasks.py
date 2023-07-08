from db import mydb


def count_words(file_path, k, row_id):
    """
    :param file_path: File path of which contents will be analyzed
    :param k: Word length to be matched with
    :param row_id: The data row which will be updated with the result
    :return: Count of words matching k length
    """
    try:
        # Opening the file in reading mode
        with open(file_path, 'r+') as file:
            # Read file content and split with space
            file_content = file.read().split()

            # Counting words matching length k
            words_with_length_k = sum(1 for word in file_content if int(len(word)) == int(k))

        # Creating a connection cursor
        cursor = mydb.cursor()

        # Updating the result in the database
        cursor.execute('''UPDATE count_log SET word_count=%s,status="Completed" WHERE id=%s''', (words_with_length_k, row_id))

        # Saving the Actions performed on the DB
        mydb.commit()

        # Closing the cursor
        cursor.close()

        return words_with_length_k
    except Exception as e:
        return e.__str__()
