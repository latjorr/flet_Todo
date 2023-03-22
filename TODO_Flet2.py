#flet boilerplate?
import flet as ft

def main(page: ft.Page):
    page.theme_mode  =  ft.ThemeMode.DARK
    page.window_height = 600
    page.window_width = 900
    
    page.title = "Flet TODO"
    
    
    page.update()

ft.app(target=main)
