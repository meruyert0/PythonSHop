# Author : Yaakov Azat @ AzatAI
# Profile: https://azat.ai/profile/yaakovazat
import time
import os
import datetime
import settings
import module

class Home():
    products = []
    current_user = settings.CURRENT_USER

    def __init__(self):
        brand = 'Welcome to AzatAI Python Shop'
        print(brand.center(100,'*'))

    def superadmin(self):
        print('')
        print(f"PLEASE CREATE A SUPER ADMIN:".center(100,' '))

    def list_user(self,role):
        """
        dasda
        :param role:
        :return:
        """
        user = module.User()
        all_users_list = user.all_users
        print("UserName UserPassword User-Date_created Admin Staff Client")
        for each in all_users_list:
            user_each_list = each.split(',')
            if user_each_list[role]:
                print(user_each_list)
    def welcome(self):
        if settings.CURRENT_USER_ROLE == 'ADMIN':
            print(f"Welcome Home {settings.CURRENT_USER_ROLE} {settings.CURRENT_USER}".rjust(100, " "))
            print("".center(100,'*'))
            print(f"SITE MANAGEMENT".center(100, ' '))
        else:
            print(f"Welcome GUEST".rjust(100,' '))
            print("".center(100,'*'))
            print(f"REGISTER/LOGIN TO CONTINUE".center(100, ' '))

