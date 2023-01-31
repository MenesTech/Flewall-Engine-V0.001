import webbrowser


def show_flw_engine(x):
    y = ["https://drive.google.com/file/d/1bnPh25Ab9q7Y0TxUqZIQW1hkWvObqpFf/view?usp=share_link", "https://drive.google.com/file/d/1N_AbQ1TxeAvSk90LNKkiQs5FrHiQDyxV/view?usp=share_link", "https://drive.google.com/file/d/18YCwlBnJ1RoB6AuJDD1-xBJiXQG8TJ1h/view?usp=share_link"
         ]
    if x == 1001:
        webbrowser.open(y[0])
    if x == 1002:
        webbrowser.open(y[1])
    if x == 1003:
        webbrowser.open(y[2])

show_flw_engine(1003)


