import os


def move_file(command: str) -> None:

    command_line = command.split(" ")

    if command_line[2].endswith("/"):
        command_line[2] = os.path.join(command_line[2],
                                       os.path.basename(command_line[1]))

    parts_of_path = command_line[2].split("/")

    if len(parts_of_path) > 1:

        folders = parts_of_path[:-1]

        new_path = ""

        for folder in folders:
            if folder:
                new_path += folder + "/"
            else:
                new_path = folder

            if not os.path.exists(new_path):
                os.mkdir(new_path)

    with (open(command_line[1], "r") as file_in,
          open(command_line[2], "w") as file_out):
        file_out.write(file_in.read())

    os.remove(command_line[1])
