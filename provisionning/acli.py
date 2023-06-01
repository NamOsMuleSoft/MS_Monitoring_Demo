import subprocess
import json
import sys

organization_id = "718f0e99-9f0c-43f6-9976-6763c79c63f0"


def call_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
    except Exception as e:
        return str(e)
    

def get_assets_from_tag(tag_name, asset_type):
    print("start")
    #--output json
    anypoint_command = 'anypoint-cli-v4 exchange:asset:list --organizationId ' + organization_id + ' --output json --limit 100 ' + tag_name
    output = call_command(anypoint_command)
    print(output)

    print("FILTER")
    filtered_assets = filter_assets_by_type(output, asset_type)
    print(filtered_assets)
    return filtered_assets
    

def filter_assets_by_type(asset_list, asset_type):
    assets = json.loads(asset_list)
    filtered_assets = [asset for asset in assets if asset['type'] == asset_type]
    return filtered_assets


def download_asset(asset):
    print("Start Download")
    download_command = 'anypoint-cli-v4 exchange:asset:download '+ asset['groupId'] + '/'  + asset['assetId'] + '/' + asset['version'] + ' ./temp'
    print (download_command)
    #call_anypoint_cli(download_command)
    print("End Download")