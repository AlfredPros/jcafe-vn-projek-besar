################################################################################
## Initialization
################################################################################

define config.mouse = { }
define config.mouse['default'] = [ ( "gui/detail/cursor.png", 0, 0) ]

init offset = -1

image delete_button_hover = im.MatrixColor("gui/menu/delete_button.png", im.matrix.brightness(+0.2))

image settings_button_hover = im.MatrixColor("gui/menu/settings_button.png", im.matrix.brightness(+0.2))

image gallery_button_hover = im.MatrixColor("gui/menu/gallery_button.png", im.matrix.brightness(+0.2))

image main_button_hover = im.MatrixColor("gui/menu/main_button.png", im.matrix.brightness(+0.2))

image load_button_hover = im.MatrixColor("gui/menu/load_button.png", im.matrix.brightness(+0.2))

image save_button_hover = im.MatrixColor("gui/menu/save_button.png", im.matrix.brightness(+0.2))

image prompt_yes_button_hover = im.MatrixColor("gui/prompt_screen/prompt_yes_button.png", im.matrix.brightness(+0.2))

image prompt_back_button_hover = im.MatrixColor("gui/prompt_screen/prompt_back_button.png", im.matrix.brightness(+0.2))

image return_button_hover = im.MatrixColor("gui/menu/return_button.png", im.matrix.brightness(+0.2))

image save_button_dark = im.MatrixColor("gui/menu/save_button.png", im.matrix.brightness(-0.5))

image main_button_dark = im.MatrixColor("gui/menu/main_button.png", im.matrix.brightness(-0.5))

transform zoom_persen(persen):
    subpixel True
    zoom persen
################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



#style ukuran_main:
    #text_size 40

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            #tambahin namebox
            add "gui/nameboxpanjang.png":
                zoom 0.5
                xpos 60
                ypos -110

            #window:
                #id "namebox"
                #style "namebox"
            text who id "who":

                text_align 0.5
                size 30
                xpos 205
                ypos -65
                color "#FFFFFF"


        if "(" and ")" in what :
            text what id "what":
                xpos 120
                color "#808080"
                size 30
                xsize 1080
        else:
            text what id "what":
                size 30
                color "#FFFFFF"
                xpos 120
                xsize 1080


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 68
    xanchor gui.name_xalign
    xsize 385
    ypos gui.name_ypos
    ysize 80
    #tambah sendiri--------------------------
    background Frame("gui/nameboxpanjang.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    #----------------------------------------
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            if i.caption == "Iya, aku tidak apa-apa. Jangan hiraukan aku dan lanjutkan rencana ":
                textbutton i.caption action i.action:
                    text_size 28
                    text_ypos -5
                    ysize 100

            elif i.caption == "Uh, aku hanya mual. Aku masih sanggup untuk mengikuti rencana.":
                textbutton i.caption action i.action:
                    text_size 28
                    text_ypos -5
                    ysize 100
            else:
                textbutton i.caption action i.action




## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu and not renpy.get_screen('choice')and renpy.get_screen('say'):

        hbox:
            xalign 0.75
            yalign 0.68
            spacing 25
            imagebutton:
                idle "gui/detail/back.png"
                action Rollback()


            imagebutton:
                idle "gui/detail/skip.png"
                action Skip() alternate Skip(fast=True, confirm=True)

            imagebutton:
                idle "gui/detail/auto.png"
                action Preference("auto-forward", "toggle")

            imagebutton:
                idle "gui/detail/save.png"
                action ShowMenu('save')

            imagebutton:
                idle "gui/detail/setting.png"
                action ShowMenu('preferences')

            imagebutton:

                idle "gui/detail/hide.png"
                action HideInterface()






## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    #frame:
        #style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    #VBOX tambahan sendiri
    add "gui/logo.png":
        zoom 0.81
        xalign -0.235 yalign -0.95
    vbox:
        spacing 10
        xalign 0.05 yalign 0.85

        textbutton _("New Game"):
            text_size 50
            action Start()

        textbutton _("Load Game"):
            text_size 50
            action ShowMenu("load")


        textbutton _("Preferences"):
            text_size 50
            action ShowMenu("preferences")

        textbutton _("Gallery"):
            text_size 50
            #nanti ganti gallery
            action ShowMenu("gallery")

        textbutton _("Quit"):
            text_size 50
            action Quit(confirm=not main_menu)
    #VBOX tambahan sendiri

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "":
                style "main_menu_title"

            text "":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):


    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
#masih bermasalah
    tag menu
    add "gui/menu/menu_save.png"
    use file_slots(_("Save"))



screen load():
# masih bermasalah
    tag menu
    add "gui/menu/menu_load.png"
    use file_slots(_("Load"))




screen file_slots(title):

    tag menu
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    if title == "Save":
        #setting button
        imagebutton:
            xalign 0.1965 yalign 0.267
            idle "gui/menu/settings_button.png"
            hover "settings_button_hover"
            action ShowMenu("preferences")

        #load button
        imagebutton:
            xalign 0.1963 yalign 0.533
            idle "gui/menu/load_button.png"
            hover "load_button_hover"
            action ShowMenu('load')

        #main menu button
        imagebutton:
            xalign 0.1963 yalign 0.666
            idle "gui/menu/main_button.png"
            hover "main_button_hover"
            action MainMenu()

        #gallery button
        imagebutton at zoom_persen(1.01) :
            xalign 0.197 yalign 0.811
            idle "gui/menu/gallery_button.png"
            hover "gallery_button_hover"
            action Show("gallery")

        #Return button
        imagebutton:
            idle "gui/menu/return_button.png"
            hover "return_button_hover"
            action Return()
            yalign 0.932



        ## The page name, which can be edited by clicking on a button.



        hbox:
            style_prefix "page"

            xalign 0.505
            yalign 0.1

            spacing gui.page_spacing


            if config.has_autosave:
                textbutton _("{#auto_page}Auto") action FilePage("auto"):
                    xpos 34
                    ypos -2
                    text_kerning -2
                    text_size 28
                    text_color "#4B0F12"
                    text_hover_color "#E3BD5B"




            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 5):
                textbutton "[page]" action FilePage(page):
                    xpos 61
                    text_color "#4B0F12"
                    text_hover_color "#E3BD5B"
                    text_size 27
                null width 7.7

            for page in range(5, 9):
                textbutton "[page]" action FilePage(page):
                    xpos 217
                    ypos 0
                    text_color "#4B0F12"
                    text_hover_color "#E3BD5B"
                    text_size 29
                null width 9.5


    else:
        #setting button
        imagebutton:
            xalign 0.1965 yalign 0.267
            idle "gui/menu/settings_button.png"
            hover "settings_button_hover"
            action ShowMenu("preferences")

        if main_menu:

            #save button dark
            add "save_button_dark":
                xalign 0.1965 yalign 0.4

        else:

            #save button
            imagebutton:
                xalign 0.1965 yalign 0.4
                idle "gui/menu/save_button.png"
                hover "save_button_hover"
                action ShowMenu('save')
        if main_menu:
            #save button dark
            add "main_button_dark":
                xalign 0.1963 yalign 0.666
        else:
            #main menu button
            imagebutton:
                xalign 0.1963 yalign 0.666
                idle "gui/menu/main_button.png"
                hover "main_button_hover"
                action MainMenu()

        #gallery button
        imagebutton at zoom_persen(1.01) :
            xalign 0.197 yalign 0.811
            idle "gui/menu/gallery_button.png"
            hover "gallery_button_hover"
            action Show("gallery")

        #Return button
        imagebutton:
            idle "gui/menu/return_button.png"
            hover "return_button_hover"
            action Return()
            yalign 0.932



        ## The page name, which can be edited by clicking on a button.

        hbox:
            style_prefix "page"

            xalign 0.505
            yalign 0.1

            spacing gui.page_spacing

            if config.has_autosave:
                textbutton _("{#auto_page}Auto") action FilePage("auto"):
                    xpos 34
                    ypos -2
                    text_kerning -2
                    text_size 28
                    text_color "#4B0F12"
                    text_hover_color "#E3BD5B"



            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 5):
                textbutton "[page]" action FilePage(page):
                    xpos 61
                    text_color "#4B0F12"
                    text_hover_color "#E3BD5B"
                    text_size 27
                null width 7.7

            for page in range(5, 9):
                textbutton "[page]" action FilePage(page):
                    xpos 217
                    ypos 0
                    text_color "#4B0F12"
                    text_hover_color "#E3BD5B"
                    text_size 29
                null width 9.5

    vbox:
        area(433,100, 770, 640)

        viewport:
            #mousewheel True

            grid 2 2:

                xspacing 104
                yspacing -30

                for i in range(2*2):

                    $ slot = i + 1

                    button:
                        # BG size: 312 x 180 px
                        #background "gui/ui/save/save.png"
                        #hover_background "gui/ui/save/save_selected.png"
                        xsize 325
                        action FileAction(slot)

                        has vbox

                        if FileLoadable(slot):

                            viewport:

                                area (0,0,347, 244)
                                add FileScreenshot(slot):
                                    xpos 0
                                    ypos 40
                                    size(297, 204)
                                imagebutton:
                                    xpos 280
                                    ypos 10
                                    idle "gui/menu/delete_button.png"
                                    hover "delete_button_hover"
                                    action FileDelete(slot)
                        else:
                            viewport:
                                area (0,0,347, 244)
                                vbox:
                                    text "Empty":
                                        xpos 118
                                        ypos 120
                                        text_align 0.5
                                        size 24
                                        font "nanifont.ttf"
                                        color "#4B0F12"
                                        hover_color "#E3BD5B"


                        null height 15

                        text FileTime(slot, format=_("{#file_time}%B %d %Y, %H:%M"), empty=_("")):  # (#file_time}%A, %B %d %Y, %H:%M
                            xalign 0.3
                            style "slot_time_text"
                            size 24
                            font "nanifont.ttf"
                            color "#4B0F12"
                            hover_color "#E3BD5B"




style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

## Gallery screen ##########################################################
#ini masih harus ditambahin buat page nya tergantung cg ada berapa
screen gallery():
    tag menu
    add "gui/menu/menu_gallery1.png"


    #inisialisasi variabel halaman
    default halaman_g = 1

    #setting button
    imagebutton:
        xalign 0.1965 yalign 0.267
        idle "gui/menu/settings_button.png"
        hover "settings_button_hover"
        action ShowMenu('preferences')

    if main_menu:

        #save button dark
        add "save_button_dark":
            xalign 0.1965 yalign 0.4

    else:

        #save button
        imagebutton:
            xalign 0.1965 yalign 0.4
            idle "gui/menu/save_button.png"
            hover "save_button_hover"
            action ShowMenu('save')

    #load button
    imagebutton:
        xalign 0.1963 yalign 0.533
        idle "gui/menu/load_button.png"
        hover "load_button_hover"
        action ShowMenu('load')

    if main_menu:
        #save button dark
        add "main_button_dark":
            xalign 0.1963 yalign 0.666
    else:
        #main menu button
        imagebutton:
            xalign 0.1963 yalign 0.666
            idle "gui/menu/main_button.png"
            hover "main_button_hover"
            action MainMenu()


    #The hell began here


    #Return button
    imagebutton:
        idle "gui/menu/return_button.png"
        hover "return_button_hover"
        action Return()
        yalign 0.932


## Credits screen###############################################################
################################################################################
## For what reason??? of course for crediting, Duh!!############################
screen kredit:
    modal True
    add "black":
        alpha 0.5

    add "gui/credit/credits.png"
    imagebutton:
        idle "gui/detail/exit.png"
        hover "gui/detail/exit.png"
        xpos 340
        ypos 130
        action Hide("kredit")

## Credits screen###############################################################
################################################################################
## For what reason??? of course for controls, Duh!!#############################
screen kontrol():
    modal True
    add "black":
        alpha 0.5

    default device = "keyboard"
    default halaman = 1

    if device == "keyboard":
        if halaman == 1:
            add "gui/controls/ctrls_keyboard1.png"

            imagebutton:
                idle "gui/detail/next_page.png"
                hover "gui/detail/next_page.png"
                xpos 1040
                ypos 125
                action SetScreenVariable("halaman",2)

        elif halaman ==2:
            add "gui/controls/ctrls_keyboard2.png"

            imagebutton:
                idle "gui/detail/previous_page.png"
                hover "gui/detail/previous_page.png"
                xpos 980
                ypos 125
                action SetScreenVariable("halaman",1)


    elif device == "mouse":
        add "gui/controls/ctrls_mouse.png"

    #button buat milih komputer ato mouse
    hbox:
        xpos 750
        ypos 110

        textbutton "Computer":
            text_font "nanifont.ttf"
            text_color "#331708"
            xsize 111
            ysize 84
            text_xalign 0.5
            text_yalign 0.5
            idle_background "gui/detail/big_idle_background.png"
            hover_background "gui/detail/big_idle_background.png"
            selected_background "gui/detail/big_selected_background.png"
            action SetScreenVariable("device", "keyboard")

        textbutton "Mouse":
            text_font "nanifont.ttf"
            text_color "#331708"
            xsize 111
            ysize 84
            text_xalign 0.5
            text_yalign 0.5
            idle_background "gui/detail/big_idle_background.png"
            hover_background "gui/detail/big_idle_background.png"
            selected_background "gui/detail/big_selected_background.png"
            action SetScreenVariable("device", "mouse")

    #exit button
    imagebutton:
        idle "gui/detail/exit.png"
        hover "gui/detail/exit.png"
        xpos 210
        ypos 125
        action Hide("kontrol")




## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    add "gui/menu/menu_settings.png"

    if main_menu:

        #save button dark
        add "save_button_dark":
            xalign 0.1965 yalign 0.4

    else:

        #save button
        imagebutton:
            xalign 0.1965 yalign 0.4
            idle "gui/menu/save_button.png"
            hover "save_button_hover"
            action ShowMenu('save')

    #load button
    imagebutton:
        xalign 0.1963 yalign 0.533
        idle "gui/menu/load_button.png"
        hover "load_button_hover"
        action ShowMenu('load')

    if main_menu:
        #save button dark
        add "main_button_dark":
            xalign 0.1963 yalign 0.666
    else:
        #main menu button
        imagebutton:
            xalign 0.1963 yalign 0.666
            idle "gui/menu/main_button.png"
            hover "main_button_hover"
            action MainMenu()

    #gallery button
    imagebutton:
        xalign 0.199 yalign 0.81
        idle "gui/menu/gallery_button.png"
        hover "gallery_button_hover"
        action Show("gallery")



    #Konten Preferences
    vbox:
        xalign 0.534
        yalign 0.292
        spacing -19
        hbox:
            #fullscreen
            textbutton "On":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16
                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("display", "fullscreen")

            textbutton "Off":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16

                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("display", "window")
        hbox:
            #skip unseen text
            textbutton "On":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16
                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("skip","all")

            textbutton "Off":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16

                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("skip", "seen")

        hbox:
            #skip after choice
            textbutton "On":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16

                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("after choices","skip")


            textbutton "Off":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16

                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("after choices", "stop")


        hbox:
            #skip Transition
            textbutton "On":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16

                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("transitions", "none")


            textbutton "Off":
                text_color "#331708"
                xsize 72
                ysize 55
                text_xalign 0.5
                text_yalign 0.45
                text_size 16

                text_font "nanifont.ttf"
                idle_background "gui/detail/idle_background.png"
                hover_background "gui/detail/idle_background.png"
                selected_background "gui/detail/selected_background.png"
                action Preference("transitions", "all")

    vbox:
        xpos 418
        ypos 458
        spacing 45
        #bar text speed
        bar value Preference("text speed"):

            xsize 329
            #sisi kiri"
            left_bar "gui/detail/filled_bar.png"
            #sisi kanan
            right_bar "gui/detail/empty_bar.png"

            #gambar tengah bar
            thumb "gui/detail/thumb.png"

            #hilangin kotak putih
            thumb_offset 15

            #pixel batas pojok thumb
            left_gutter 16
            right_gutter 16

        #bar auto speed
        bar value Preference("auto-forward time"):
            xsize 329
            #sisi kiri"
            left_bar "gui/detail/filled_bar.png"
            #sisi kanan
            right_bar "gui/detail/empty_bar.png"

            #gambar tengah bar
            thumb "gui/detail/thumb.png"

            #hilangin kotak putih
            thumb_offset 15

            #pixel batas pojok thumb
            left_gutter 16
            right_gutter 16

    # buat rollback side
    hbox:
        xpos 855
        ypos 151
        spacing -3

        textbutton "Disable":
            text_font "nanifont.ttf"
            text_color "#331708"
            xsize 111
            ysize 84
            text_xalign 0.5
            text_yalign 0.5
            idle_background "gui/detail/big_idle_background.png"
            hover_background "gui/detail/big_idle_background.png"
            selected_background "gui/detail/big_selected_background.png"
            action Preference("rollback side", "disable")

        textbutton "Left":
            text_font "nanifont.ttf"
            text_color "#331708"
            xsize 111
            ysize 84
            text_xalign 0.5
            text_yalign 0.5
            idle_background "gui/detail/big_idle_background.png"
            hover_background "gui/detail/big_idle_background.png"
            selected_background "gui/detail/big_selected_background.png"
            action Preference("rollback side", "left")

        textbutton "Right":
            text_font "nanifont.ttf"
            text_color "#331708"
            xsize 111
            ysize 84
            text_xalign 0.5
            text_yalign 0.5
            idle_background "gui/detail/big_idle_background.png"
            hover_background "gui/detail/big_idle_background.png"
            selected_background "gui/detail/big_selected_background.png"
            action Preference("rollback side", "right")

    vbox:
        xpos 857
        ypos 345
        spacing 43

        #bar sound, music, voice
        bar value Preference("music volume"):

            xsize 329
            #sisi kiri"
            left_bar "gui/detail/filled_bar.png"
            #sisi kanan
            right_bar "gui/detail/empty_bar.png"

            #gambar tengah bar
            thumb "gui/detail/thumb.png"

            #hilangin kotak putih
            thumb_offset 15

            #pixel batas pojok thumb
            left_gutter 16
            right_gutter 16

        bar value Preference("sound volume"):

            xsize 329
            #sisi kiri"
            left_bar "gui/detail/filled_bar.png"
            #sisi kanan
            right_bar "gui/detail/empty_bar.png"

            #gambar tengah bar
            thumb "gui/detail/thumb.png"

            #hilangin kotak putih
            thumb_offset 15

            #pixel batas pojok thumb
            left_gutter 16
            right_gutter 16

        bar value Preference("voice volume"):

            xsize 329
            #sisi kiri"
            left_bar "gui/detail/filled_bar.png"
            #sisi kanan
            right_bar "gui/detail/empty_bar.png"

            #gambar tengah bar
            thumb "gui/detail/thumb.png"

            #hilangin kotak putih
            thumb_offset 15

            #pixel batas pojok thumb
            left_gutter 16
            right_gutter 16

    hbox:
        #buat menu controls sama credit di pojok kanan bawah
        xpos 890
        ypos 500
        spacing 37

        textbutton "Controls":
            text_font "nanifont.ttf"
            text_color "#331708"
            xsize 111
            ysize 84
            text_xalign 0.5
            text_yalign 0.5
            idle_background "gui/detail/big_idle_background.png"
            hover_background "gui/detail/big_idle_background.png"
            selected_background "gui/detail/big_selected_background.png"
            action ShowMenu("kontrol")

        textbutton "Credits":
            text_font "nanifont.ttf"
            text_color "#331708"
            xsize 111
            ysize 84
            text_xalign 0.5
            text_yalign 0.5
            idle_background "gui/detail/big_idle_background.png"
            hover_background "gui/detail/big_idle_background.png"
            selected_background "gui/detail/big_selected_background.png"
            action ShowMenu("kredit")


    #return button
    imagebutton:
        idle "gui/menu/return_button.png"
        hover "return_button_hover"
        action Return()
        yalign 0.932


screen preferences_backup():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")


            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help


screen keyboard_help():

    add "gui/controls/ctrls_keyboard1.png":
        xalign -0.5 yalign 0.0

screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200
    add "black":
        alpha 0.75
    #main menu
    if message == "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.":
        add "gui/prompt_screen/prompt_backmainmenu.png":
            align (0.5,0.5)
            zoom 0.75
        imagebutton at zoom_persen(0.75):
            xalign 0.5
            yalign 0.61
            idle "gui/prompt_screen/prompt_yes_button.png"
            hover "prompt_yes_button_hover"
            action yes_action
        imagebutton at zoom_persen(0.75):
            xalign 0.64
            yalign 0.61
            idle "gui/prompt_screen/prompt_back_button.png"
            hover "prompt_back_button_hover"
            action no_action

    #quit game
    elif message == "Are you sure you want to quit?":
        add "gui/prompt_screen/prompt_exitgame.png":
            align (0.5,0.5)
            zoom 0.75
        imagebutton at zoom_persen(0.75):
            xalign 0.5
            yalign 0.61
            idle "gui/prompt_screen/prompt_yes_button.png"
            hover "prompt_yes_button_hover"
            action yes_action
        imagebutton at zoom_persen(0.75):
            xalign 0.64
            yalign 0.61
            idle "gui/prompt_screen/prompt_back_button.png"
            hover "prompt_back_button_hover"
            action no_action

    #overrite save
    elif message == "Are you sure you want to overwrite your save?":
        add "gui/prompt_screen/prompt_overwritesave.png":
            align (0.5,0.5)
            zoom 0.75
        imagebutton at zoom_persen(0.75):
            xalign 0.5
            yalign 0.61
            idle "gui/prompt_screen/prompt_yes_button.png"
            hover "prompt_yes_button_hover"
            action yes_action
        imagebutton at zoom_persen(0.75):
            xalign 0.64
            yalign 0.61
            idle "gui/prompt_screen/prompt_back_button.png"
            hover "prompt_back_button_hover"
            action no_action

    #buat load ditengah game
    elif message == "Loading will lose unsaved progress.\nAre you sure you want to do this?":
        add "gui/prompt_screen/prompt_load_in_game.png":
            align (0.5,0.5)
            zoom 0.75
        imagebutton at zoom_persen(0.75):
            xalign 0.5
            yalign 0.61
            idle "gui/prompt_screen/prompt_yes_button.png"
            hover "prompt_yes_button_hover"
            action yes_action
        imagebutton at zoom_persen(0.75):
            xalign 0.64
            yalign 0.61
            idle "gui/prompt_screen/prompt_back_button.png"
            hover "prompt_back_button_hover"
            action no_action

    #buat delete save
    elif message == "Are you sure you want to delete this save?":
        add "gui/prompt_screen/prompt_delete_save.png":
            align (0.5,0.5)
            zoom 0.75
        imagebutton at zoom_persen(0.75):
            xalign 0.5
            yalign 0.61
            idle "gui/prompt_screen/prompt_yes_button.png"
            hover "prompt_yes_button_hover"
            action yes_action
        imagebutton at zoom_persen(0.75):
            xalign 0.64
            yalign 0.61
            idle "gui/prompt_screen/prompt_back_button.png"
            hover "prompt_back_button_hover"
            action no_action



    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    add "gui/detail/notif.png":
        ysize 80
        xsize 240
        align (0,0)

    hbox:
        xpos 30
        ypos 34
        spacing 10

        text _("Skipping"):
            font "nanifont.ttf"
            size 24
            yoffset -4
            outlines [(absolute(1), "567B49", 0,0)]

        add "gui/detail/skip_indicator.png"
        add "gui/detail/skip_indicator.png"
        add "gui/detail/skip_indicator.png"

## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    add "gui/detail/notif.png":
        ysize 80

    text "[message!tq]":
        font "nanifont.ttf"
        size 23
        xpos 70
        ypos 30

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
