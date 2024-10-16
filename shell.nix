{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
    buildInputs = with pkgs; [
        python3
        python3Packages.pip
        python3Packages.torch
        python3Packages.numpy
    ];

    shellHook = ''
        export PS1="(env) \[\033[0;34m\]\w> \[\033[0;37m\]"
    '';
}
