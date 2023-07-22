import dearpygui.dearpygui as gui
import pymem
#Memory
pm = pymem.Pymem('hl2.exe')
client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll

OffEntityList = 0x0071957C
OffLocalPlayer = pm.read_uint(client + 0x006FD274)
OffHealth = 0x90
OffTeam = 0x9C
OffCoordsX = 0x314
OffCoordsY = 0x324
OffCoordsZ = 0x334

#Code
def on_refresh(sender, data):
    onlineply = 0
    with gui.window(label='Nexus', width=370, height=400, no_title_bar=True, no_resize=True, no_move=True):
        with gui.tab_bar(label='Tabs'):
            with gui.tab(label='PlayerList'):
                gui.add_button(label="Refresh", callback=on_refresh)
                for i in range(64):
                    entity = pm.read_uint(client + OffEntityList + i * 0x10)
                    if entity != 0:
                        onlineply = onlineply + 1
                        Health = pm.read_uint(entity + OffHealth)
                        Team = pm.read_uint(entity + OffTeam)
                        CoordsX = pm.read_float(entity + OffCoordsX)
                        CoordsY = pm.read_float(entity + OffCoordsY)
                        CoordsZ = pm.read_float(entity + OffCoordsZ)
                        MyCoordsX = pm.read_float(OffLocalPlayer + OffCoordsX)

                        if MyCoordsX == CoordsX:
                            with gui.collapsing_header(label= f"ID: {i} (You!)"):
                                gui.add_text(f"Health: {Health} | Team: {Team}")
                                gui.add_text(f"Coordinates:")
                                gui.add_text(f"- X: {CoordsX}")
                                gui.add_text(f"- Y: {CoordsY}")
                                gui.add_text(f"- Z: {CoordsZ}")

                        else:
                            with gui.collapsing_header(label= f"ID: {i}"):
                                gui.add_text(f"Health: {Health}  |  Team: {Team}")
                                gui.add_text(f"Coordinates:")
                                gui.add_text(f"- X: {CoordsX}")
                                gui.add_text(f"- Y: {CoordsY}")
                                gui.add_text(f"- Z: {CoordsZ}")

                gui.add_text("")
                gui.add_text(f"Online Players: {onlineply}")
                gui.add_text("")
                gui.add_text("")
            with gui.tab(label="About"):
                gui.add_text("Version : 0.1")
                # https://github.com/Calvineries/gmod-external-playerlist
                gui.add_text("GitHub Page : github.com/Calvineries\n/gmod-external-playerlist")            
                gui.add_text("")
                gui.add_text("Author : Calvineries")
                gui.add_text("Contributors: ...")

#GUI
gui.create_context()
gui.create_viewport(title='External GMOD PlayerList', decorated=True, width=370, height=400)
gui.set_viewport_resizable(False)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)

with gui.window(label='Nexus', width=370, height=400, no_title_bar=True, no_resize=True, no_move=True):
    with gui.tab_bar(label='Tabs'):

        with gui.tab(label='PlayerList'):
            gui.add_button(label="Refresh", callback=on_refresh)
        with gui.tab(label="About"):
            gui.add_text("Version : 0.1")
            # https://github.com/Calvineries/gmod-external-playerlist
            gui.add_text("GitHub Page : github.com/Calvineries\n/gmod-external-playerlist")            
            gui.add_text("")
            gui.add_text("Author : Calvineries")
            gui.add_text("Contributors: ...")

gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()
