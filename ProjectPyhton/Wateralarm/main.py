
import time
from plyer import notification
if __name__== "__main__":
    while True:
        notification.notify(
            title = "Drinking Time",
            message = "Water is your body's principal chemical component and makes up about 50% to 70% of your body weight. Your body depends on water to survive.", 
            # app_icon = (r"C:\Users\anmol\OneDrive\Desktop\project3\icon.ico"), 
            timeout=2
            
        )
        time.sleep(6)
        # time.sleep(60*60)