from subprocess import call

with open("tar_files", "r") as target_file:
    for line in target_file:
        call(("tar", "-xvf", line.strip()))
