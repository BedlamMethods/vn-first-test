define  n = Character("Noriko", color="#27963f")
define m = Character("[player_name]", who_color="#00aaff")
define narrator = Character(None)

label start:
    stop music fadeout 1.0
    scene bg empty
    "What do you want to be called?"
    menu:
        
        "Enter your name":
            $ player_name = renpy.input("Enter your name:", length=15).strip()
            if not player_name:
                $ player_name = "Meikyo"

        "Use default name (Meikyo)":
            $ player_name = "Meikyo"

    scene bg roof
    show noriko idle at left

    n "Let's always be together, [player_name]."

    m "*nods.* Yes, I promise." # Player Speech

    narrator "A promise was whispered on the school rooftop, just before the {color=#ff0000}Estimated Night.{/color}"
    menu:

        "start the Estimated Night.":
            jump estimated_night
        "start Grave scene.":
            jump grave_scene
        "mini game":
            jump minigame  
    
label estimated_night:
    scene bg street
    show noriko happy
    n "thank you for walking me home"

    return
label grave_scene:
    scene bg graveyard
    show noriko sad
    n "you promised to always be with me, but now you're gone."
    return
label minigame:
    scene bg minigame
    
    return
