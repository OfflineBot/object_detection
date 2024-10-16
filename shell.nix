{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
    buildInputs = with pkgs; [
        python3
        python3Packages.pip
        python3Packages.torch
        python3Packages.numpy
        python3Packages.pillow
        python3Packages.matplotlib
    ];

    shellHook = ''
        export PS1="(shell) \[\033[0;34m\]\w> \[\033[0;37m\]"
    '';
}
