import rich.console, rich.panel, rich.prompt

def client_header_layout():
    client_header = rich.panel.Panel('',title='CLIENT')
    rich.console.console.print(client_header)

def server_header_layout():
    server_headert = rich.panel.Panel('',title='SERVER')
    rich.console.console.print(server_headert)
