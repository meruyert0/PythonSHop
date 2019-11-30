import time
import control


class User():
    """
    This is the blue print of User Instance
    """
    user_name = ''
    user_pw = ''
    date_created = ''
    is_admin = False
    is_staff = False
    is_client = False
    all_users = []

    def __init__(self):
        with open('data/users.txt','r') as f:
            user_data = f.read()
        user_list = user_data.strip('\n').split('\n')
        self.all_users = user_list

    def add(self,user_name, user_pw):
        """
        bla bal
        :param user_name:
        :param user_pw:
        :return:
        """
        time_format = "%Y-%m-%d %X %A %B %p %r"
        time_current = time.strftime(time_format)
        self.user_name = user_name
        self.user_pw = user_pw
        self.date_created = time_current
        user_string = f"{self.user_name},{self.user_pw},{self.date_created},{self.is_admin},{self.is_staff},{self.is_client}"
        log_message = f"Created new User: {user_string}"
        control.logger(log_message)
        with open("data/users.txt",'a') as f:
            f.write(user_string)
            f.write('\n')
        self.__init__()
