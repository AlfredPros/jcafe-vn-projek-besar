transform enter:
    subpixel True
    zoom 0.80
    align(0.5, 1.0)
    alpha 0.0
    ease 0.3 zoom 0.85 alpha 1.0

    on hide:
        ease 0.3 zoom 0.72 alpha 0.0

transform bounce:
    subpixel True
    ease 0.1 yoffset 40
    ease 0.1 yoffset 0

    on hide:
        ease 0.3 zoom 0.72 alpha 0.0

transform talk:
    subpixel True
    ease 0.3 zoom 0.9 yalign 1.0

    on hide:
        ease 0.3 zoom 0.72 alpha 0.0

transform notalk:
    subpixel True
    ease 0.3 zoom 0.85 yalign 1.0

    on hide:
        ease 0.3 zoom 0.72 alpha 0.0

transform close_up:
    subpixel True
    ease 0.5 zoom 1.7 yalign 2.0

transform push_away:
    subpixel True
    ease 0.4 zoom 0.85 yalign 1.0

transform sigh:
    subpixel True
    easein_cubic 0.8 yoffset 30

transform normal:
    subpixel True
    ease 0.3 yoffset 0

transform item_show:
    subpixel True
    alpha 0
    align (0.0, 0.0)
    zoom 0.8
    ease 0.3 alpha 1.0 zoom 1.0

#character move lol

transform m34:
    subpixel True
    ease 0.5 xalign 1.3

transform m03:
    subpixel True
    xalign -1.0
    ease 0.8 xalign 0.5

transform m02:
    subpixel True
    xalign -1.0
    ease 0.8 xalign -0.3

transform leave1:
    subpixel True

    on hide:
        ease 1.3 xalign -1.5
        pause 1
        alpha 0.0

transform m4:
    subpixel True
    pause 0.5
    ease 0.3 xalign 0.90
transform m2:
    subpixel True
    pause 0.5
    ease 0.3 xalign 0.10

transform aa:
    subpixel True
    ease 0.3 xalign 0.5
