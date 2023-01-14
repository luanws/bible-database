from pymenu import auto_menu

menu = auto_menu.create_menu_from_directory('scripts')
menu.add_option('exit', exit)
menu.show()
