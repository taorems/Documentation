# Introduction

This is the introduction to using Docfx for source code documentation.  

## Quickstart

This is a quick setup guide on how to spin up the application.

### Dev Run
To run an instance of the app with a database included, run the powershell script run.dev.ps1.

To access the swagger interface go to http://localhost:8080/docs

Below the procedure to create an asset are described.

A utility script is provided to create an asset and add operations to it. This script is located in the /app/utils/ folder and is called add_asset.py. The fastapi server needs to be running for it to work. The script can be run with the following command:

```bash
docker exec CONTAINER_ID python ./app/utils/add_asset.py
```

Where CONTAINER_ID is the ID of the container running the fastapi server, you can find this with `docker ps`.