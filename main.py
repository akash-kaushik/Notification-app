import time   # Import Time module to get the time
from win10toast import ToastNotifier  # Import Notifier to push notification

def ask_user_about_time_interval():
    """Ask the time of water interval in minutes and convert in seconds"""
    ak_u_ab_tme_int = False
    while not ak_u_ab_tme_int:
        user_time_water = input("Enter the Time Interval You want to Drink Water in Minutes:")
        if user_time_water.isdigit():
            user_time_water = int(user_time_water)
            user_time_water = user_time_water*60
            ak_u_ab_tme_int =True
    return user_time_water

def water_notification():
    water_title = "Water Notification"
    water_dec = "Drink Water Please!"
    water_ntf = ToastNotifier()
    water_ntf.show_toast(water_title, water_dec, icon_path ="./water_notification_icon.ico")

def custom_notification(j, k):
    cus_title = f"Custom Notification {j}"
    cus_dec = k
    custom_ntf = ToastNotifier()
    custom_ntf.show_toast(cus_title, cus_dec, icon_path = "./custom_notification_icon.ico")

def custom_notification_time():
    """ This ask for the Time of the Custom Notification! """

    cut_not_tme = False
    while not cut_not_tme:
        print("Enter the Time:")
        hour = input("Enter the Hour (12 hr format):")
        if hour.isdigit() and int(hour) > 0 and int(hour) < 13:
            mint = input("Enter the Minute:")
            if mint.isdigit() and int(mint) >= 0 and int(mint) < 61:
                tym = input("AM or PM:").upper()
                if tym == "AM" or tym == "PM":
                    cut_not_tme = True
    if int(hour) < 10 and int(mint) < 10:
        time_text = f"0{hour} : 0{mint} {tym}"
    elif int(hour) >= 10 and int(mint) < 10:
        time_text = f"{hour} : 0{mint} {tym}"
    elif int(hour) < 10 and int(mint) >= 10:
        time_text = f"0{hour} : {mint} {tym}"
    else:
        time_text = f"{hour} : {mint} {tym}"

    return time_text

def custom_notification_mess():
    text_mess = input("Please enter the Custom Message:")
    return text_mess

def ask_custom_notification():
    """ This ask the user want a Custom Notification or Not ! """

    cus_ntf = False
    while not cus_ntf:
        ntf = input("Do you want Custom Notification:").lower()
        if ntf == "y" or ntf == "yes":
            cus_ntf = True
            return True
        elif ntf == "n" or ntf == "no":
            cus_ntf = True
            return False

def list_custom_notification(m, n):
    time_taken = custom_notification_time()
    m.append(time_taken)
    mess_taken = custom_notification_mess()
    n.append(mess_taken)
    return m, n

def ask_custom_notification_number():
    want_cus_ntf_num = False
    while not want_cus_ntf_num:
        cus_ntf_num = input("Enter the Number of Custom Notification: ")
        if cus_ntf_num.isdigit():
            cus_ntf_num = int(cus_ntf_num)
            want_cus_ntf_num = True
        else:
            print("Please provide a correct Input!")
    return cus_ntf_num


if __name__ == '__main__':
    """ It is the Main function! """

    init_water = time.time()     # Give a time

    want_cus_ntf = ask_custom_notification()

    cus_time_list = []
    cus_mess_list = []

    if want_cus_ntf:
        """ Ask Number of Custom Notification  """

        try:
            num_cus_notf = ask_custom_notification_number()
            if num_cus_notf > 0:

                for i in range(num_cus_notf):
                    cus_time_list, cus_mess_list = list_custom_notification(cus_time_list, cus_mess_list)
                want_cus_ntf = False

        except:
            print("You Provide incorrect Input!")
            want_cus_ntf = False
    else:
        cus_time_list.append("0")
        cus_mess_list.append("Notification")
        num_cus_notf = 0

    c_tym_in = 0

    time_interval = ask_user_about_time_interval()      # Ask Time interval of water notification
    while True:

        if time.time() - init_water > time_interval:
            """ Water Notification """

            water_notification()
            time.sleep(10)
            init_water = time.time()

        current_tym = time.strftime("%I : %M %p")   # Getting current time in 12hr format by system
        if num_cus_notf != 0:
            """ Custom Time Notification """
            if current_tym == cus_time_list[c_tym_in]:
                custom_notification(cus_time_list[c_tym_in], cus_mess_list[c_tym_in])
                num_cus_notf = num_cus_notf - 1
                c_tym_in = c_tym_in + 1