#Type su before running this
mkdir ~/repos

#'Homemade' repos
mkdir ~/repos/gcryptor_repo
mkdir ~/repos/cryptor_repo
mkdir ~/repos/pcal_repo
mkdir ~/repos/configs
mkdir ~/repos/mfc_repo

mkdir ~/repos/

git clone https://github.com/simo002m/GCryptor.git ~/repos/gcryptor_repo
git clone https://github.com/simo002m/Cryptor.git ~/repos/cryptor_repo
git clone https://github.com/simo002m/PCal.git ~/repos/pcal_repo
git clone https://github.com/simo002m/configs.git ~/repos/configs
git clone https://github.com/simo002m/mfc.git ~/repos/mfc_repo

git clone https://github.com/LinxGem33/Plank-Themes.git ~/

apt-add-repository ppa:noobslab/macbuntu
apt-get update

programs=(vim tmux python3-tk plank mate-terminal albert plank openssh-server virtualbox dmenu macbuntu-os-icons-lts-v7 macbuntu-os-ithemes-lts-v7 macbuntu-os-plank-theme-lts-v7 links2 nsnake arduino idle3 emacs leafpad ipython3 gcolor2)

for ((i=0; i < ${#programs[*]}; i++))
do
	sudo apt-get install -y $i
done
