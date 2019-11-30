from pyzt import inputi,inputs,inputf
import platform
import settings

if __name__ == '__main__':
    if platform.python_version()[0] == '3':
        import control
        control=control.Control()
        if settings.DEBUG:
            print("DEBUG MODE")
        else:
            control.run()
    else:
        exit("SHOP: Unsupported Python Version!")

