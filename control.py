## THIS IS THE CCONTROLLER FILE< IT IS TH SUPERSET SUPER FATHER OF THE MODULE AND VIEW IT THIS PROJECT
import time
import settings
import platform
import subprocess
import view
import module
from pyzt import inputs, inputi, inputf


def logger(message):
    time_format  = "%Y-%m-%d %X %A %B %p %r"
    time_current = time.strftime(time_format)
    with open('data/log.txt','a') as f:
        f.write(f"{time_current}:{message}")
        f.write('\n')

class Control():
    fr = settings.FIRST_RUN
    current_user = 'Azat' #Current user in this session
    current_user_role = 'admin'

    def prepare_file(self,log='data/log.txt',users='data/users.txt',products='data/products.txt',orders='data/orders.txt'):
        path_list = [log,orders,products,users]
        for each in path_list:
            with open(each,'w') as f:
                f.write('')

    def system_check(self):
        # check python version
        print(f"Step 1: Checking Python Version : {platform.python_version()}")
        if platform.python_version()[0] == '3':
            print('PYTHON VERSION OK!')
        else:
            exit('Sorry, The program dose not support your python version, please update to python3.x')
        # check required packages installed
        print(f"Step 2: Checking Python packages")
        required_pkgs = ['azt','pyzt']
        installed_pkgs = subprocess.check_output(['pip3','list']).decode("utf-8")
        for pkg in required_pkgs:
            if pkg not in installed_pkgs:
                exit("requirements not installed! Please install all of required packages.")
            print("PYTHON PACKAGE REQUIREMENTS OK!")
        print(f"Step 3: Checking data resources")
        data_resources = ['data/log.txt','data/users.txt','data/products.txt','data/orders.txt']
        for each in data_resources:
            try:
                with open(each) as f:
                    pass
            except FileNotFoundError:
                exit("Data Source NOt Found!")

    def run(self):
        print("Running the AzatAI Python Shop system self checking")
        self.system_check()
        self.prepare_file()
        if self.fr is False: # super admin already exist
            print("In the case super admin already exist")
            # TODO
        else:
            home = view.Home()
            home.superadmin()
            user_name = inputs('Please input a username for SUPERADMIN:\n')
            user_pw = inputs(f'Please input a password for SUPERADMIN {user_name}:\n')
            user = module.User()
            user.is_admin = True
            user.add(user_name,user_pw)
            settings.SUPER_ADMIN = user_name
            settings.SUPER_ADMIN_PW = user_pw
            settings.CURRENT_USER = user_name
            settings.CURRENT_USER_ROLE = "ADMIN"
            self.admin()

            # TODO
    def admin(self):
        home_admin = view.Home()
        home_admin.welcome()
        admin_choice = inputi("Please select your choice\n")
        print(admin_choice)
        home_admin.list_user(3)