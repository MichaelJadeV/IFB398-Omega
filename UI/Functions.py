
def change_to_FileName():
    """
    This function swaps from the quiz
    frame to the work frame.
    :return: Nothing
    """
    Frame1.forget()
    Frame3.pack(fill='both', expand=1)

def change_to_save():
    Frame3.forget()
    Frame4.pack(fill='both', expand=1)

def return_to_menu():
    Frame4.forget()
    Frame5.forget()
    Frame1.pack(fill='both', expand =1)

def view_data():
    Frame1.forget()
    Frame5.pack(fill='both', expand = 1)