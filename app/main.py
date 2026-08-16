import os


def move_file(command: str) -> None:

    command_line = command.split(" ")

    if len(command_line) < 3 or command_line[0] != "mv":
        return

    if (command_line[2].endswith("/")
            or command_line[2].endswith("\\")
            or os.path.isdir(command_line[2])):
        command_line[2] = os.path.join(command_line[2],
                                       os.path.basename(command_line[1]))

    directory = os.path.dirname(command_line[2])

    if directory:
        os.makedirs(directory, exist_ok=True)

    with (open(command_line[1], "r") as file_in,
          open(command_line[2], "w") as file_out):
        file_out.write(file_in.read())

    os.remove(command_line[1])
