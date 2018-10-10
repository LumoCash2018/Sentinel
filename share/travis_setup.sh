#!/bin/bash
set -evx

mkdir ~/.lumocashcore

# safety check
if [ ! -f ~/.lumocashcore/.lumocash.conf ]; then
  cp share/lumocash.conf.example ~/.lumocashcore/lumocash.conf
fi
