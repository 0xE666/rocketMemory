import os, sys, time
from datetime import datetime

try:
    import pymem
    import pymem.process
    from pattern import *
    import pymem.memory
    from pymem.process import module_from_name
    from pymem.ptypes import RemotePointer
    from datetime import datetime
except ImportError:
    print('Attempting to install PyMem')
    os.system('python -m pip install pymem')

import pymem
import pymem.process
import pymem.pattern
import pymem.memory
from pattern import *
from pymem.process import module_from_name
from pymem.ptypes import RemotePointer

p = pymem.Pymem()
p.open_process_from_name("RocketLeague.exe")
os.system('cls')

def timeStamp():
    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    return timestamp

def resolve_pointer(base, offsets):
    last = base
    for offset in offsets:
        last = RemotePointer(p.process_handle, last.value + offset)
    return last.v.value


def steam():
    os.system('cls')
    e1 = " " * 25 + "███████╗    ███████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗"
    e2 = " " * 25 + "██╔════╝    ██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝"
    e3 = " " * 25 + "█████╗█████╗█████╗     ██║   ██║   ██║██║   ██║██║     ███████╗"
    e4 = " " * 25 + "██╔══╝╚════╝██╔══╝     ██║   ██║   ██║██║   ██║██║     ╚════██║"
    e5 = " " * 25 + "███████╗    ███████╗██╗██║   ╚██████╔╝╚██████╔╝███████╗███████║"
    e6 = " " * 25 + "╚══════╝    ╚══════╝╚═╝╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝"

    print('\n')
    print(" " * 25 + '-' * 64)
    print('\n')
    print(e1)
    time.sleep(0.1)
    print(e2)
    time.sleep(0.1)
    print(e3)
    time.sleep(0.1)
    print(e4)
    time.sleep(0.1)
    print(e5)
    time.sleep(0.1)
    print(e6)
    time.sleep(0.1)
    print('\n')
    print(" " * 45 + 'rocketMemory - made by e')
    print(" " * 25 + '-' * 64)
    time.sleep(2)
    os.system('cls')


    print(f"\r[{timeStamp()}] Succesfully Hooked To RocketLeague.exe ({p.process_handle})")
    module = pymem.process.module_from_name(p.process_handle, "RocketLeague.exe")
    baseAddr = module_from_name(p.process_handle, "RocketLeague.exe").lpBaseOfDll
    max_address = module.lpBaseOfDll + module.SizeOfImage
    print(f"\r[{timeStamp()}] Scanning for settings pointer.")
    settingsPattern = b'\x80\x42\x00\x00\x43\x02\x00\x00\x60\x00\x3a\x44\x43\x00\x00\x00\x80\x54\x26\x00\x00\x02\x00\x00\x00\xf5'
    settingsScan = pattern_scan_module(p.process_handle, module, settingsPattern, "xx??xxxxx?xxx?xxxxx??xxxxx")
    if settingsScan:
        print(f"\r[{timeStamp()}] Succesfully grabbed settings address. ({'0x{:X}'.format(settingsScan)})")
        settingsAddr = "0x{:X}".format(settingsScan)
        settingsAddress = int(settingsScan) - int(baseAddr)
        print(f"\r[{timeStamp()}] Succesfully grabbed settings pointer. ({'0x{:X}'.format(settingsAddress)})")

    settingsBase = RemotePointer(p.process_handle, module_from_name(p.process_handle, "RocketLeague.exe").lpBaseOfDll + settingsAddress)

    fovPTR = resolve_pointer(settingsBase, [0xF0])
    fovValue = p.read_float(fovPTR)
    print(f'FOV: {int(fovValue)}')

    #distance pointer address found with offset
    distancePTR = resolve_pointer(settingsBase, [0xFC])
    distanceValue = p.read_float(distancePTR)
    print(f'Distance: {int(distanceValue)}')

    #height pointer address found with offset
    heightPTR = resolve_pointer(settingsBase, [0xF4])
    heightValue = p.read_float(heightPTR)
    print(f'Height: {int(heightValue)}')

    #angle pointer address found with offset
    anglePTR = resolve_pointer(settingsBase, [0xF8])
    angleValue = p.read_float(anglePTR)
    print(f'Angle: {int(angleValue)}\n\n')

    change = input('which setting would you like to change?\nFOV\nDistance\nHeight\nAngle\n:> ')
    if 'fov' in change.lower():
        changeVal = input('\nEnter Value for FOV: ')
        fovPTR = resolve_pointer(settingsBase, [0xF0])
        p.write_float(fovPTR, float(changeVal))
        fovValue = p.read_float(fovPTR)
        print(f'New Value: {fovValue}, if not updating toggle ballcam :)')
        time.sleep(5)
        steam()
    if 'distance' in change.lower():
        changeVal = input('\nEnter Value for Distance: ')
        distancePTR = resolve_pointer(settingsBase, [0xFC])
        p.write_float(distancePTR, float(changeVal))
        distanceVal = p.read_float(distancePTR)
        print(f'New Value: {distanceVal}, if not updating toggle ballcam :)')
        time.sleep(5)
        steam()
    if 'height' in change.lower():
        changeVal = input('\nEnter Value for Height: ')
        heightPTR = resolve_pointer(settingsBase, [0xF4])
        p.write_float(heightPTR, float(changeVal))
        heightVal = p.read_float(heightPTR)
        print(f'New Value: {distanceVal}, if not updating toggle ballcam :)')
        time.sleep(5)
        steam()
    if 'angle' in change.lower():
        changeVal = input('\nEnter Value for Height: ')
        anglePTR = resolve_pointer(settingsBase, [0xF8])
        p.write_float(anglePTR, float(changeVal))
        angleVal = p.read_float(anglePTR)
        print(f'New Value: {angleVal}, if not updating toggle ballcam :)')
        time.sleep(5)
        steam()

def epic():
    os.system('cls')
    e1 = " " * 25 + "███████╗    ███████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗"
    e2 = " " * 25 + "██╔════╝    ██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝"
    e3 = " " * 25 + "█████╗█████╗█████╗     ██║   ██║   ██║██║   ██║██║     ███████╗"
    e4 = " " * 25 + "██╔══╝╚════╝██╔══╝     ██║   ██║   ██║██║   ██║██║     ╚════██║"
    e5 = " " * 25 + "███████╗    ███████╗██╗██║   ╚██████╔╝╚██████╔╝███████╗███████║"
    e6 = " " * 25 + "╚══════╝    ╚══════╝╚═╝╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝"

    print('\n')
    print(" " * 25 + '-' * 64)
    print('\n')
    print(e1)
    time.sleep(0.1)
    print(e2)
    time.sleep(0.1)
    print(e3)
    time.sleep(0.1)
    print(e4)
    time.sleep(0.1)
    print(e5)
    time.sleep(0.1)
    print(e6)
    time.sleep(0.1)
    print('\n')
    print(" " * 45 + 'rocketMemory - made by e')
    print(" " * 25 + '-' * 64)
    time.sleep(2)
    os.system('cls')

    print(f"\r[{timeStamp()}] Succesfully Hooked To RocketLeague.exe ({p.process_handle})")
    module = pymem.process.module_from_name(p.process_handle, "RocketLeague.exe")
    baseAddr = module_from_name(p.process_handle, "RocketLeague.exe").lpBaseOfDll
    max_address = module.lpBaseOfDll + module.SizeOfImage
    print(f"\r[{timeStamp()}] Scanning for settings pointer.")
    settingsPattern = b'\x00\xeb\x6a\x00\x71\x00\x00\x00\x00\xf2\x6a\x00\x71\x00\x00\x00\x00\xe4'
    settingsScan = pattern_scan_module(p.process_handle, module, settingsPattern, "xxx?x?xxxxx?x?xxxx")
    if settingsScan:
        print(f"\r[{timeStamp()}] Succesfully grabbed settings address. ({'0x{:X}'.format(settingsScan)})")
        settingsAddr = "0x{:X}".format(settingsScan)
        settingsAddress = int(settingsScan) - int(baseAddr)
        print(f"\r[{timeStamp()}] Succesfully grabbed settings pointer. ({'0x{:X}'.format(settingsAddress)})")

    settingsBase = RemotePointer(p.process_handle, module_from_name(p.process_handle, "RocketLeague.exe").lpBaseOfDll + settingsAddress)

    fovPTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xF0])
    fovValue = p.read_float(fovPTR)
    print(f'FOV: {int(fovValue)}')

    #distance pointer address found with offset
    distancePTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xFC])
    distanceValue = p.read_float(distancePTR)
    print(f'Distance: {int(distanceValue)}')

    #height pointer address found with offset
    heightPTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xF4])
    heightValue = p.read_float(heightPTR)
    print(f'Height: {int(heightValue)}')

    #angle pointer address found with offset
    anglePTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xF8])
    angleValue = p.read_float(anglePTR)
    print(f'Angle: {int(angleValue)}\n\n')
    change = input('which setting would you like to change?\nFOV\nDistance\nHeight\nAngle\n:> ')
    if 'fov' in change.lower():
        changeVal = input('\nEnter Value for FOV: ')
        fovPTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xF0])
        p.write_float(fovPTR, float(changeVal))
        fovValue = p.read_float(fovPTR)
        print(f'New Value: {fovValue}, if not updating toggle ballcam :)')
        time.sleep(5)
        epic()
    if 'distance' in change.lower():
        changeVal = input('\nEnter Value for Distance: ')
        distancePTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xFC])
        p.write_float(distancePTR, float(changeVal))
        distanceVal = p.read_float(distancePTR)
        print(f'New Value: {distanceVal}, if not updating toggle ballcam :)')
        time.sleep(5)
        epic()
    if 'height' in change.lower():
        changeVal = input('\nEnter Value for Height: ')
        heightPTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xF4])
        p.write_float(heightPTR, float(changeVal))
        heightVal = p.read_float(heightPTR)
        print(f'New Value: {distanceVal}, if not updating toggle ballcam :)')
        time.sleep(5)
        epic()
    if 'angle' in change.lower():
        changeVal = input('\nEnter Value for Height: ')
        anglePTR = resolve_pointer(settingsBase, [0x450, 0x10, 0x2D0, 0x170, 0x270, 0x380, 0x1F8, 0xF8])
        p.write_float(anglePTR, float(changeVal))
        angleVal = p.read_float(anglePTR)
        print(f'New Value: {angleVal}, if not updating toggle ballcam :)')
        time.sleep(5)
        epic()

choice = input('Steam or Epic Games :> ')
if 'steam' in choice.lower():
    steam()
if 'epic' in choice.lower():
    epic()
