#!/bin/bash

# gitコマンドの補完
wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -O ~/.git-completion.bash
cat <<EOF >> ~/.bashrc

# git command completion
source $HOME/.git-completion.bash
EOF

exit 0
