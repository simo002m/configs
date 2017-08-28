from subprocess import call

call(["mkdir", "~/repos"])

#'Homemade' repos
call(["mkdir", "~/repos/gcryptor_repo"])
call(["mkdir", "~/repos/cryptor_repo"])
call(["mkdir", "~/repos/mfc_repo"])
call(["mkdir", "~/repos/configs"])


git clone https://github.com/simo002m/GCryptor.git ~/repos/gcryptor_repo
git clone https://github.com/simo002m/Cryptor.git ~/repos/cryptor_repo
git clone https://github.com/simo002m/PCal.git ~/repos/pcal_repo
git clone https://github.com/simo002m/configs.git ~/repos/configs
git clone https://github.com/simo002m/mfc.git ~/repos/mfc_repo

git clone https://github.com/LinxGem33/Plank-Themes.git ~/

call(["apt-add-repository", "ppa:noobslab/macbuntu"])
call(["apt-get", "update"])

program_list = [vim, tmux, python3-tk, python3-pip, plank, mate-terminal, albert, plank, openssh-server, virtualbox, dmenu, macbuntu-os-icons-lts-v7, macbuntu-os-ithemes-lts-v7, macbuntu-os-plank-theme-lts-v7, w3m, w3m-img, links2, nsnake, idle3, emacs, leafpad, ipython3, gcolor2]

for program in program_list:
	call(["sudo", "apt", "install", "-y", program])
