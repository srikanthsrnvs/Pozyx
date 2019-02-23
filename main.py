#import pypozyx
import sys, time
from pypozyx import PozyxSerial, get_first_pozyx_serial_port, POZYX_SUCCESS, SingleRegister, EulerAngles, Acceleration, UWBSettings
#pozyx = PozyxLib()  # PozyxSerial has PozyxLib's functions, just for generality
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
is_cursor_up = False
#print(pypozyx.get_first_pozyx_serial_port())
pozyx = PozyxSerial(get_first_pozyx_serial_port())
who_am_i = SingleRegister()
# get the data, passing along the container
status = pozyx.getWhoAmI(who_am_i)
acceleration = Acceleration()
euler_angles = EulerAngles()
uwb_settings = UWBSettings()

# check the status to see if the read was successful. Handling failure is covered later.
if status == POZYX_SUCCESS:
    # print the container. Note how a SingleRegister will print as a hex string by default.
    print('Who Am I: {}'.format(who_am_i)) # will print '0x43'

while True:
    # initalize the Pozyx as above

    # initialize the data container

    # and repeat
    # initialize the data container
    # get the data, passing along the container
    if is_cursor_up:
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
    pozyx.getAcceleration_mg(acceleration)
    print('Accleration: {}'.format(acceleration))

    # initialize the data container
    # get the data, passing along the container
    sys.stdout.write(ERASE_LINE)
    pozyx.getEulerAngles_deg(euler_angles)
    print('Euler Angle: {}'.format(euler_angles))
    sys.stdout.write(ERASE_LINE)
    pozyx.getUWBSettings(uwb_settings)
    print('UWB Settings: {}'.format(uwb_settings), end='\r')
    time.sleep(1)
    is_cursor_up =True
