from subprocess import call

call(["mkdir", "~/repos"])

# directories for 'homemade' repos
dirs = ["gcryptor", "cryptor", "mfc", "mfc_cli", "configs"]

for directory in dirs: 
    call(["mkdir", "~/repos/", directory])

repos = {
        "gcryptor":["https://github.com/simo002m/GCryptor.git", "~/repos/gcryptor"],
        "cryptor":["https://github.com/simo002m/Cryptor.git", "~/repos/cryptor"],
        "mfc_cli":["https://github.com/simo002m/mfc_cli.git", "~/repos/mfc_cli"],
        "mfc":["https://github.com/simo002m/mfc.git", "~/repos/mfc"],
        "configs":["https://github.com/simo002m/configs.git", "~/repos/configs"],

        "plank_themes":["https://github.com/LinxGem33/Plank-Themes.git" "~/"]
        }

for repo in repos:
    call(["git", "clone", repo])


call(["apt-add-repository", "ppa:noobslab/macbuntu"])
call(["apt-get", "update"])

program_list = ["vim", "tmux", "python3-tk", "python3-pip", "plank", "mate-terminal", "albert", "openssh-server", "virtualbox", "dmenu", "macbuntu-os-icons-lts-v7", "macbuntu-os-ithemes-lts-v7", "macbuntu-os-plank-theme-lts-v7", "w3m", "w3m-img", "links2", "nsnake", "idle3", "emacs", "leafpad", "ipython3", "gcolor2"]

for program in program_list:
	call(["sudo", "apt", "install", "-y", program])
