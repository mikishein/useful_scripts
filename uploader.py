from posixpath import basename
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext
import os
BASEURL         = "https://bsmach.sharepoint.com"
BASESITE        = '/sites/cybcourse/' # every share point has a home.
SITEURL         = BASEURL + BASESITE
COURSE_FOLDER   = "CybCBbFolders"


def upload_file(file_content,user_folder, ctx):
    
    dir, name = os.path.split(user_folder)
    # Create folder if not exsitent
    ctx.web.folders.add(dir).execute_query()
    # Upload file
    ctx.web.get_folder_by_server_relative_url(dir).upload_file(name,
     file_content).execute_query()
def main():
    username = input("Enter username: ")
    password = input("Enter pass: ")

    # Authentication
    ctx_auth = AuthenticationContext(SITEURL)
    ctx_auth.acquire_token_for_user(username, password)
    ctx = ClientContext(SITEURL, ctx_auth)

    folder = input("enter dir to folder: ")
    files = [os.path.join(folder[1:-1],x) for x in os.listdir(folder[1:-1])]
    for file in files:
        with open(file,"r",encoding="utf8") as report:
            report_content = report.read()
            print(os.path.basename(file)[:9])
            upload_file(report_content.encode(),
            f"{COURSE_FOLDER}\\{os.path.basename(file)[:9]}\\{os.path.basename(file)}",
            ctx)
if __name__ == "__main__":
    main()