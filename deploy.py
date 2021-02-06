import os
import shutil


class Deploy:

    def run(self):
        # run defined commands, pull FMETemplate2 and lib64
        for cmd in self.app_config["cmd_bat"]:
            cmd_line = cmd.replace("code_path", self.app_config["code_path"]) \
                .replace("app_name", self.app_config["app_name"]).replace("lib_name", self.app_config["lib_name"]) \
                .replace("git_path", self.app_config["git_path"]).replace("python_path", self.app_config["python_path"])
            os.system(cmd_line)

        # copy secret config file
        shutil.copy(self.app_config["secret_src"], self.app_config["secret_dest"])
        print("Copying file: %s" % self.app_config["secret_dest"])

    def __init__(self, app_config):
        self.app_config = app_config
