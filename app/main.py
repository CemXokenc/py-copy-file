def copy_file(command: str) -> None:
    try:
        command_list = command.split(" ")

        if command_list[0] != "cp" or command_list[1] == command_list[2]:
            return

        try:
            with (
                open(command_list[1], "r") as file_in,
                open(command_list[2], "w") as file_out
            ):
                file_out.write(file_in.read())
        except FileNotFoundError:
            return
    except IndexError:
        return
