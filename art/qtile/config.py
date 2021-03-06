###################################################
################# Arthur Finkelmann ###############
###################################################

import os
import re
import socket
import subprocess
import os.path
import cairocffi
#from xdg.IconTheme import getIconPath
from libqtile.config import Key, Screen, Group, Match, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer, base

from typing import List  # noqa: F401


mod = "mod4"
home = os.path.expanduser('~')

keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod, "shift"], "c", lazy.spawn("chromium")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "q", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),

    Key([mod], "p", lazy.spawn("./Scripts/pmenu.sh")),

    Key([mod, "shift"], "f", lazy.spawn("firefox")),
    Key([mod], "d", lazy.spawn("rofi -show run")),

    #Backlight controla
    Key([mod], "Down", lazy.spawn("sudo light -U 5")),
    Key([mod], "Up", lazy.spawn("sudo light -A 5")),

    #Volume control
    Key([mod], "Left", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([mod], "Right", lazy.spawn("amixer -c 0 -q set Master 2dB+")),

    #Change keyboard layout
    Key([mod], "space", lazy.spawn("./Scripts/kbdlayout.sh")),

    #File Explorer
    Key([mod],"e",lazy.spawn("thunar")),    
    Key([mod,"shift"],"e",lazy.spawn("sudo thunar")),

]


groups = [
    Group("1", label=""),
    Group("2", matches=[Match(wm_class=["firefox"])], label=""),
    Group("3", matches=[Match(wm_class=["code-oss"])], label=""),
    Group("4", label=""),
   # Group("5",matches=[Match(wm_class=['chrom'])] label=""),
    ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(border_focus = "5e81ac", border_normal = "b48ead", border_width = 3, margin = 5,),
    layout.MonadWide(border_focus = "5e81ac", border_normal = "b48ead", border_width = 3, margin = 5,),
]

widget_defaults = dict(
    font='Cascadia Code',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [Screen(top=bar.Bar([

                widget.GroupBox(
                    background = "2e3440",
                    active = "5e81ac",
                    inactive = "b48ead",
                    this_current_screen_border = "bf616a",
                    highlight_method = "line",
                    highlight_color=["2e3440", "2e3440"],
                    center_aligned=True,),
                
                widget.Prompt(),
                
                widget.Sep(background = "2e3440"),
                
                widget.TaskList(
                    background = "2e3440",
                    foreground = "2e3440",
                    border = "5e81ac",
                    unfocused_border = "b48ead",
                    highlight_method = "block",
                    max_title_width=100,
                    title_width_method="uniform",
                    rounded=False
                    ),
            

                widget.Systray(background = "2e3440"),
               
                #Key Bord Leyout 0 
                widget.TextBox(
                    text='',
                    background="2e3440",
                    foreground="8fbcbb",
                    padding=0, 
                    fontsize=37),
                
                widget.TextBox(
                    text=' ',
                    background="8fbcbb",
                    foreground="2e3440",
                    ),
                
                widget.KeyboardLayout(
                    background="8fbcbb",
                    foreground="2e3440",
                    padding=4),
                #Volumen 2
                widget.TextBox(
                    text='',
                    background="8fbcbb",
                    foreground="ebcb8b",
                    padding=0,
                    fontsize=37),
                
                widget.TextBox(
                    text=' ', 
                    background="ebcb8b",
                    foreground="2e3440",
                    padding=2),
                
                widget.Volume(
                    background="ebcb8b",
                    foreground="2e3440",
                    padding=4),
                #Backlight 3
                widget.TextBox(
                    text='',
                    background="ebcb8b",
                    foreground="88c0d0",
                    padding=0,
                    fontsize=37),
                
                widget.TextBox(
                    text=' ', 
                    background="88c0d0",
                    foreground="2e3440",
                    padding=2),
                
                widget.Backlight(
                    background="88c0d0",
                    foreground="2e3440",
                    padding=4,
                    backlight_name="intel_backlight"),

                widget.TextBox(
                    text='',
                   background="88c0d0",
                    foreground="aebe8c",
                    padding=0,
                    fontsize=37),
                
                widget.TextBox(
                    text=' ',
                    background="aebe8c",
                    foreground="2e3440",
                    padding=2),
                
                widget.Clock(
                    format='%a  %H:%M ',
                    background = "a3be8c",
                    foreground = "2e3440",
                    pading=4),

                widget.TextBox(
                    text='',
                    background="a3be8c",
                    foreground="bf616a",
                    padding=0,
                    fontsize=37),
                
                widget.TextBox(
                    text=' ', 
                    background="bf616a",
                    foreground="2e3440",
                    padding=2),
                
                widget.Wlan(
                    background="bf6a6a",
                    foreground="2e3440",
                    padding=4,
                    interface='wlo1',
                    format='{essid} {percent:2.0%}',
                    ),               
           
                widget.Net(
                    interface='wlo1',
                    foreground='2e3440',
                    background='bf6a6a',
                   ),
            
                widget.TextBox(
                    text='',
                    background="bf6a6a",
                    foreground="88c0d0",
                    padding=0,
                    fontsize=37),
                
                widget.TextBox(
                        text='🔋',
                    background="88c0d0",
                    foreground="2e3440",
                    padding=2),
                           
               widget.Battery(
                 update_inverval=5,
                 battery="BAT0",
                 format='{char} {percent:2.0%} ',
                # charge_char='⇧ ', 
                 charge_char=u"\U0001F50C",
                 discharge_char='⇩',
                 empty_char='☐',
                 full_char= u"\U0001F50B",             
                 background="88c0d0",
                 foreground="2e3440",
                 padding=4,
                update_interval=1,      
                show_short_text='false',
                ),
               
                ],
            size=24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

def wallpaper():
    path = '~/background/wallpaper.png'
    os.system('feh --bg-scale ' + path)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
    os.system('./Scripts/setWallpaper')
    os.system('setxkbmap de')



