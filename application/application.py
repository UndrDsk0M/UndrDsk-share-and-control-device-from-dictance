from dearpygui.dearpygui import *
import threading 
import pyautogui
import io
import PIL.Image as Image
import functools 
from time import sleep

create_context()


with font_registry():
    welcomeSign_font = add_font("./VeganStylePersonalUse-5Y58.ttf", 40)
    bold_font = add_font("./Merriweather-Bold.ttf", 20)
    welcomeText_font = add_font("./VeganStylePersonalUse-5Y58.ttf", 5)
    digital_font = add_font('./digital-7.ttf', 10)
    defualt_font = add_font("./Merriweather-Black.ttf", 15)

create_viewport(title="UndrDsk", width=800, height=600, resizable=False)

with theme() as global_theme:
    with theme_component(mvAll):
        add_theme_color(mvThemeCol_WindowBg, (45, 66, 99), category=mvThemeCat_Core)

@functools.lru_cache(maxsize = None) 
def screenshot1():
    while True:
        pyautogui.screenshot().save('./cash.png')
        byteImgIO = io.BytesIO()
        byteImg = Image.open('./cash.png')
        byteImg.save(byteImgIO, "PNG")
        byteImgIO.seek(0)
        byteImgIO.read()   
        screenshot1.cache_clear()
        

t1 = threading.Thread(target=screenshot1)


def from_welcome_go_control():
    global welcomePage
    delete_item(item=welcomePage)
    controlWindow()

def from_welcome_go_client():
    delete_item(item=welcomePage)
    clientWindow()
    
def from_client_go_welcome():
    global welcomePage
    delete_item(item=clientPage)
    welcomeWindow()

def from_control_go_welcome():
    delete_item(item=controlPage)
    welcomeWindow()

def from_control1_go_control2():
    delete_item(item=controlPage)
    welcomeWindow()

def from_client1_go_client2():
    delete_item(clientPage)
    clientWindow2()

def from_client2_go_welcome():
    delete_item(item=clientPage2)
    welcomeWindow()


def SearchJoinCode():
    try :
        delete_item('loading')
        add_loading_indicator(parent="clientpage",pos=(350, 380),tag="loading", color=(0, 242, 255),  secondary_color=(0, 255, 47), speed=6)
    
        print(get_value('joincode'))
        from_client1_go_client2()
        hide_item('keyboard_searchjoincode')
    except:
        print("test")

 

def controlWindow():
    global controlPage
    with window (    
        no_move=True,
        no_close=True,
        no_resize=True,
        no_title_bar=True,
        width=800,
        height=600,
        pos=(0,0),
        tag="controlpage",) as controlPage:
        with menu_bar():
            add_menu_item(label="Home", callback=from_control_go_welcome)
            with menu(label="Help"):
                add_text("""
                        Hello guys,
                        this is UndrDsk windows app
                        what does it do ? Great qustion

                        it is very simple app to use with simple ui
                        imagin we have two windows computer's at two diffrent place ( C1(first computer) and C2 )

                        C1 is us and C2 is our grandma(Its not possible for me(RIP))
                        our grandma cannot found her old pictures she needs some help, 
                        but how can we help her? with UndrDsk!
                        
                        UndrDsk helps you control mouse and keyboard 
                        and see other share screen with less problems and cost!
                                                                        """)
                with menu(label="This Page Help"):
                    add_menu_item(label="In this page you should Enter the code that controller created")
            add_menu_item(label="Client", callback=from_control_go_welcome)
            add_menu_item(label="* Controller")
            add_menu_item(label="info")
        add_button(label="<", callback=from_client_go_welcome, pos=(5, 200),width=25)
        add_text("by @UndrDskM",color=(88, 138, 140), pos=(365,560))


with handler_registry(tag="keyboard_searchjoincode") as handler:
    add_key_release_handler(callback=SearchJoinCode)


def clientWindow():
    global clientPage
    with window (
        no_move=True,
        no_close=True,
        no_resize=True,
        no_title_bar=True,
        width=800,
        height=600,
        pos=(0,0),
        tag="clientpage",) as clientPage:

        with menu_bar():
            add_menu_item(label="Home", callback=from_client_go_welcome)
            with menu(label="Help"):
                add_text("""
                        Hello guys,
                        this is UndrDsk windows app
                        what does it do ? Great qustion

                        it is very simple app to use with simple ui
                        imagin we have two windows computer's at two diffrent place ( C1(first computer) and C2 )

                        C1 is us and C2 is our grandma(Its not possible for me(RIP))
                        our grandma cannot found her old pictures she needs some help, 
                        but how can we help her? with UndrDsk!
                        
                        UndrDsk helps you control mouse and keyboard 
                        and see other share screen with less problems and cost!
                                                                        """)
                with menu(label="This Page Help"):
                    add_menu_item(label="In this page you should Enter the code that controller created")
            add_menu_item(label="* Client")
            add_menu_item(label="Controller", callback=from_client_go_welcome)
            add_menu_item(label="info")
        
        add_button(label="<", callback=from_client_go_welcome, pos=(5, 200),width=25)
        add_input_text(label="Enter Join-Code",no_spaces=True, tag="joincode", pos=(100,200))
        add_loading_indicator(pos=(380, 380),tag="loading", color=(0, 255, 47),  secondary_color=(0, 242, 255))
        add_text("by @UndrDskM",color=(88, 138, 140), pos=(365,560))

# bind_item_handler_registry('joincode', "keyboard_searchjoincode")


def clientWindow2():
    global clientPage2
    with window (
        no_move=True,
        no_close=True,
        no_resize=True,
        no_title_bar=True,
        width=800,
        height=600,
        pos=(0,0),
        tag="clientpage2",) as clientPage2:
        with menu_bar():
            add_menu_item(label="Home", callback=from_client2_go_welcome)
            with menu(label="Help"):
                add_text("""
                        Hello guys,
                        this is UndrDsk windows app
                        what does it do ? Great qustion

                        it is very simple app to use with simple ui
                        imagin we have two windows computer's at two diffrent place ( C1(first computer) and C2 )

                        C1 is us and C2 is our grandma(Its not possible for me(RIP))
                        our grandma cannot found her old pictures she needs some help, 
                        but how can we help her? with UndrDsk!
                        
                        UndrDsk helps you control mouse and keyboard 
                        and see other share screen with less problems and cost!
                                                                        """)
                with menu(label="This Page Help"):
                    add_menu_item(label="In this page you should Do nothing and give control ro controller")
            add_menu_item(label="> Client")            
            add_menu_item(label="info")    
        add_text("by @UndrDskM",color=(88, 138, 140), pos=(365,560))
        add_button(label="Close Call", pos=(0,0), width=200, height=100, callback=stop_dearpygui)
        t1.start()

        set_viewport_pos((0,0))
        set_viewport_height(200)
        set_viewport_width(300)
        set_viewport_always_top(True)
        set_viewport_resizable(False)


def welcomeWindow():
    global welcomePage
    with window(
        no_move=True,
        no_close=True,
        no_resize=True,
        no_title_bar=True,
        width=800,
        height=600,
        pos=(0,0),
        tag="logpage") as welcomePage:
        with menu_bar():
            add_menu_item(label="Home")
            with menu(label="Help"):
                add_text("""
                        Hello guys,
                        this is UndrDsk windows app
                        what does it do ? Great qustion

                        it is very simple app to use with simple ui
                        imagin we have two windows computer's at two diffrent place ( C1(first computer) and C2 )

                        C1 is us and C2 is our grandma(Its not possible for me(RIP))
                        our grandma cannot found her old pictures she needs some help, 
                        but how can we help her? with UndrDsk!
                        
                        UndrDsk helps you control mouse and keyboard 
                        and see other share screen with less problems and cost!
                                                                        """)
                with menu(label="This Page Help"):
                    add_menu_item(label="In this page you should choose you are grandma or not\n * Client (who is controlled (Grandma)\n * Controller (who controlls))")
            add_menu_item(label="Client", callback=from_welcome_go_client)
            add_menu_item(label="Controller", callback=from_welcome_go_control)
            add_menu_item(label="info")

            



        welcomesign = add_text("Welcome To UndrDsk", pos=(210,90))
        client_button = add_button(label="Client" ,width=200,height=100,pos=(225,300), callback=from_welcome_go_client)
        controller_button = add_button(label="Controller" ,width=200,height=100,pos=(425,300), callback=from_welcome_go_control)
        add_text("by @UndrDskM",color=(88, 138, 140), pos=(365,560))
        
        
        bind_item_font(welcomesign, welcomeSign_font)
        bind_item_font(client_button, bold_font)
        bind_item_font(controller_button, bold_font)


        






# Apply the custom theme
bind_theme(global_theme)
bind_font(defualt_font)
# Setup and show viewport
welcomeWindow()
setup_dearpygui()
show_viewport()

# Start Dear PyGui
start_dearpygui()

# Destroy context
destroy_context()
