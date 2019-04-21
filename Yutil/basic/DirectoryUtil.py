# -*- coding: utf-8 -*-

import os
import shutil

#def is_current_path_format(path):


def make_dir(path:str, remake_flag = False):
    if os.path.isdir(path):
        if remake_flag:
            shutil.rmtree(path)
        else:
            return
    os.mkdir(path)
#END make_dir


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
指定のパスに指定のディレクトリ構成を作成する
@param    path:str 作成したいパスを記載する
@param    dir_tree_dict:dict ディレクトリ構成を記載する
@return  void
===sample start ====
path = "PATH"
dir_tree_dict = {
    "a": {
        "ab":None,
        "ac":None,
    },
    "b":None,
}
make_dir_tree_structure(path, dir_tree_dict)
---output---
PATH
├── a
│   ├── ab
│   └── ac
└── b
===sample end ===
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def make_dir_tree_structure(path:str, dir_tree_dict:dict):
    make_dir(path)
    if dir_tree_dict is None:
        return False
    for key,value in dir_tree_dict.items():
        make_dir_tree_structure(path+"/"+key, value)
#END make_dir_tree_structure

if __name__ == '__main__':
    #make_dir("sample", ignore_all_flag = True)
    tree_dict = {
        "a": {
            "ab":None,
            "ac":None,
        },

        "b":None,
    }
    make_dir_tree_structure("sample", tree_dict)