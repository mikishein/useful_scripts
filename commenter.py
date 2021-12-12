# Imports
import zipfile
import os
# Constants
HTML = """
     \n<div>
      \n<br><br>
      \n<h3 align="right">&nbsp;&nbsp;&nbsp;הערה ראשית - ##</h3>
      \n<br>
     \n</div>
"""
COMMENT_INEDX = 9
def main():
    test_name = input("Enter the test name: (step1/tars3 ana aaref...)")
    path_to_zip_file = input("Enter path to zip file: ")
    dir_name = f"{os.path.dirname(path_to_zip_file)}\{os.path.basename(path_to_zip_file).split('.')[0]}"[1:]
    # Check if folder already exists
    if not os.path.exists(dir_name):
        path_to_zip_file = fr"{path_to_zip_file}"[1:-1]
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            os.mkdir(dir_name)
            zip_ref.extractall(dir_name)
            for report in os.listdir(dir_name):
                filea = os.path.join(dir_name,report)
                os.rename(os.path.join(dir_name,report),os.path.join(dir_name,f"{test_name}_{report[-8:]}"))
    number = input("Enter student number: ")
    while number.lower() != "exit":
        report_file = os.path.join(dir_name,f"step3_{number}.html")
        report_content = ""
        with open(report_file,'r',encoding="utf8") as report:
            report_content = report.readlines()
        with open(report_file,'w',encoding="utf8") as report:
            comment = input("Enter master comment for student: ")
            finish = input("happy with the comment? y/n ")
            while finish.lower() == "n":
                comment = input("Enter master comment for student: ")
                finish = input("wanna try again? y/n ")
            after_format = HTML.replace("##",comment)
            report_content[COMMENT_INEDX] = after_format
            with_comment = "".join(report_content)
            report.write(with_comment)
        number = input("Enter student number: ")
if __name__ == "__main__":
    main()