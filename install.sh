#!/bin/bash

BINS="/usr/local/bin/"

echo "Are you using Termux? y/n"
read termux

if [ $termux == "y" ];
then
	BINS="/data/data/com.termux/files/usr/bin/"
fi



is_installed(){
	if [ -f "${BINS}aquelarre" ]; 
	then
		true
	else
		false
	fi	
}

if is_installed;
then
	echo 'Aquelarre is already installed.'
	echo 'Want to unistall it? y/n'
	read user_input
	if [ $user_input == "y" ];
	then
		echo "Removing..."
		rm "${BINS}aquelarre_syntax.py"
		rm "${BINS}aquelarre_interpreter.py"
		rm "${BINS}aquelarre_server.py" 
		rm "${BINS}aquelarre"
		echo 'Removed!'
	fi
else
	echo 'Installing...'
	cp aquelarre_syntax.py $BINS
	cp aquelarre_interpreter.py $BINS
	cp aquelarre_server.py $BINS
	cp aquelarre $BINS
	echo 'Installed!'
fi
