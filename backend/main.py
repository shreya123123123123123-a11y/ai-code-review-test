from fastapi import FastAPI, Request

from github_client import get_pull_request_files


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Code Reviewer Running"
    }



@app.post("/github-webhook")
async def github_webhook(request: Request):

    data = await request.json()


    print("GitHub Event Received:")
    print(data)


    action = data.get("action")


    if action == "opened":

        repo_name = data["repository"]["full_name"]

        pr_number = data["pull_request"]["number"]


        files = get_pull_request_files(
            repo_name,
            pr_number
        )


        print("Changed Files:")
        print(files)



    return {
        "message": "Webhook received successfully"
    }