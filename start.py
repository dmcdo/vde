import json
import os


def cmdline(container_name):
    with open(f".\\.containers\\{container_name}\\config.json") as file:
        conf = json.load(file)

        commandline = f"qemu-system-{conf['architecture']}"

        for flag, value in conf['flags'].items():
            for v in value if type(value) is list else [value]:
                commandline += f" -{flag} {v if v else ''}"

        return commandline


def start(container_name):
    cl = cmdline(container_name)

    os.chdir(f".\\.containers\\{container_name}")
    os.system(cl)
    os.chdir("..\\..")
