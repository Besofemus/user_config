#!/usr/bin/env python3

import i3
import winswitch

if __name__ == "__main__":
    
    memorycons = i3.move_windows("tmp")

    i3.focus_workspace("tmp")

    winid = winswitch.choose_window()
    
    i3.restore_workspaces(memorycons);
    
    i3.focus_window(winid)

