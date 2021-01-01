def login_back_frame():
    return """
    QPushButton{
    border: none;
    margin-right: 7% auto;
    border-radius: 15%;
    width: 30%;
    height: 30%;
    }
    
    QPushButton::hover{
        background-color : #9999FF;
        color: #000000;
    }

    QPushButton::pressed{
    background-color: #4e6486;
    }
    """

# #################


def main_frame():
    return """    
    background-color: #23272a;
    border-radius: 20%;
    padding: 6px;
    color: white;
    """


def line_edit():
    return """
    border: none;
    border-bottom: 1px solid #A1A1A1;
    """


def log_button():
    return """
    QPushButton{
    background-color: #AA0000;
    border-radius: 5%;
    border:solid #A1A1A1;
    }
    QPushButton::hover{
    background-color : #cc0066;
    }
    QPushButton::pressed{
    background-color: #4e6486;
    }
    """


def left_layout_student():
    """
    border-radius: 7%;
    border-bottom: 1px solid #FFFFFF;
    """
    return """
    QFrame{
    background-color: #0066CC;
    color: #FFFFFF;
    }

    QLabel{
    color: #000000;
    }

    QPushButton{
    border: none;
    text-align: left;
    padding: 5%;
    color: white;
    border-radius: 7%;
    }

    QPushButton::hover{
        background-color : #9999FF;
        color: #000000;
    }

    QPushButton::focus{
    background-color: #4e6486;
    }

    """


def right_layout_student():
    return """
    QFrame{
    background-color: #009999;
    border-radius: 20%;
    }

    QPushButton{
    border: none;
    margin-right: 7% auto;
    border-radius: 15%;
    width: 30%;
    height: 30%;
    }

    QPushButton::hover{
        background-color : #9999FF;
        color: #000000;
    }

    QPushButton::pressed{
    background-color: #4e6486;
    }

    QLineEdit{
    border: none;
    background-color: #009999;
    border-bottom: 1px solid #FFFFFF;
    color: #000000
    }
    """


def item_bottom_layout():
    return """
    QFrame{
    border-radius: 7%;
    }
    """


def group_box_student():
    return """
    QGroupBox{
    background-color: #4e6486;
    border-radius: 7%;
    color: #FFFFFF;
    }

    QLineEdit{
    border: none;
    border-bottom: 1px solid #A1A1A1;
    background-color: #4e6486;
    }

    QComboBox{
    background-color: #4F5070;
    color: #FFFFFF;
    }

    QLabel{
    color: #FFFFFF;
    }
    """


def group_box_teacher():
    return """
    QGroupBox{
    background-color: #055050;
    border-radius: 7%;
    color: #FFFFFF;
    }

    QLineEdit{
    border: none;
    border-bottom: 1px solid #A1A1A1;
    background-color: #055050;
    }

    QComboBox{
    background-color: #4F5070;
    color: #FFFFFF;
    }

    QLabel{
    color: #FFFFFF;
    }
    """


def dashboard_frame():
    return """
    .QFrame{
    background-color: #055050;
    border-bottom: 3px solid #AA0000;
    }
    QLabel{
    color: #FFFFFF;
    }
    """