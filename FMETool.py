import os
import json
import clean_lib
import deploy

CONFIG = "app.json"

app_config = {}
# read app settings
with open(CONFIG) as app_config_json:
    app_config = json.load(app_config_json)
    # populate combined values
    app_config["lib_path"] = os.path.join(app_config["code_path"], app_config["app_name"], app_config["lib_name"])
    app_config["secret_src"] = app_config["secret_src"] % app_config["secret_name"]
    app_config["secret_dest"] = os.path.join(app_config["code_path"], app_config["app_name"],
                                             app_config["secrets_dir_name"],
                                             app_config["secret_name"])

# deploy files
deploy_job = deploy.Deploy(app_config)
deploy_job.run()
# remove extra dir and file in lib64
clean_job = clean_lib.CleanLib(app_config)
clean_job.clean_lib()
