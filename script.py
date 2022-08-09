# Python program to demonstrate
# command line arguments


import getopt, sys
import os

# Extenstions according to type of file
document = [
    ".doc",
    ".docx",
    ".pdf",
    ".txt",
    ".rtf",
    ".html",
    ".htm",
    ".ods",
    ".ppt",
    ".pptx",
]
image = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".svg",
    ".psd",
    ".raw",
    ".webp",
    ".ico",
    ".ai",
    ".eps",
]
video = [
    ".avi",
    ".mp4",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    ".vob",
    ".ogv",
    ".ogg",
    ".mpg",
    ".mpeg",
    ".m4v",
    ".3gp",
    ".3g2",
]
audio = [
    ".mp3",
    ".wav",
    ".aac",
    ".flac",
    ".wma",
    ".m4a",
    ".alac",
    ".ogg",
    ".oga",
    ".mid",
    ".midi",
    ".rtttl",
    ".rtx",
    ".ota",
    ".imy",
    ".mka",
]
executable = [
    ".exe",
    ".msi",
    ".apk",
    ".app",
    ".bat",
    ".com",
    ".jar",
    ".wsf",
    ".vb",
    ".vbs",
    ".vbe",
    ".js",
    ".jse",
    ".ps1",
    ".ps1xml",
    ".ps2",
    ".ps2xml",
    ".psc1",
    ".psc2",
    ".msc",
    ".msh",
    ".msh1",
    ".msh2",
    ".mshxml",
    ".msh1xml",
    ".msh2xml",
    ".scf",
    ".lnk",
    ".inf",
    ".reg",
    ".pif",
    ".url",
    ".wsc",
    ".sct",
    ".wsh",
    ".ps1",
    ".ps1xml",
    ".ps2",
    ".ps2xml",
    ".psc1",
    ".psc2",
    ".msc",
    ".msh",
    ".msh1",
    ".msh2",
    ".mshxml",
    ".msh1xml",
    ".msh2xml",
    ".scf",
    ".lnk",
    ".inf",
    ".reg",
    ".pif",
    ".url",
    ".wsc",
    ".sct",
    ".wsh",
]
compressed = [
    ".zip",
    ".rar",
    ".7z",
    ".gz",
    ".bz2",
    ".tar",
    ".tgz",
    ".xz",
    ".z",
    ".Z",
    ".7zip",
    ".ace",
    ".arj",
    ".bz",
    ".cab",
    ".dmg",
    ".iso",
    ".jar",
    ".lzh",
    ".pkg",
    ".rar",
    ".sit",
    ".sitx",
    ".tar",
    ".tar.gz",
    ".tar.bz2",
    ".tar.xz",
    ".tar.Z",
    ".zip",
    ".zipx",
    ".zoo",
    ".zpaq",
    ".7z",
    ".ace",
    ".arj",
    ".bz",
    ".cab",
    ".dmg",
    ".iso",
    ".jar",
    ".lzh",
    ".pkg",
    ".rar",
    ".sit",
    ".sitx",
    ".tar",
    ".tar.gz",
    ".tar.bz2",
    ".tar.xz",
    ".tar.Z",
    ".zip",
    ".zipx",
    ".zoo",
    ".zpaq",
]


# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "f:"

# Long options
long_options = ["Folder"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-f", "--Folder"):
            path = currentValue

            # get files in the folder
            files = os.listdir(path)
            for file in files:

                # get file extension and organize it to folders
                fileExtension = os.path.splitext(file)[1]
                if fileExtension in document:
                    # create folder if it doesn't exist
                    if not os.path.exists(path + "/documents"):
                        os.makedirs(path + "/documents")
                    os.rename(path + "/" + file, path + "/" + "documents/" + file)
                elif fileExtension in image:
                    if not os.path.exists(path + "/images"):
                        os.makedirs(path + "/images")
                    os.rename(path + "/" + file, path + "/" + "images/" + file)
                elif fileExtension in video:
                    if not os.path.exists(path + "/videos"):
                        os.makedirs(path + "/videos")
                    os.rename(path + "/" + file, path + "/" + "videos/" + file)
                elif fileExtension in audio:
                    if not os.path.exists(path + "/audio"):
                        os.makedirs(path + "/audio")
                    os.rename(path + "/" + file, path + "/" + "audio/" + file)
                elif fileExtension in executable:
                    if not os.path.exists(path + "/executables"):
                        os.makedirs(path + "/executables")
                    os.rename(path + "/" + file, path + "/" + "executables/" + file)
                elif fileExtension in compressed:
                    if not os.path.exists(path + "/compressed"):
                        os.makedirs(path + "/compressed")
                    os.rename(path + "/" + file, path + "/" + "compressed/" + file)
                else:
                    if not os.path.exists(path + "/others"):
                        os.makedirs(path + "/others")
                    os.rename(path + "/" + file, path + "/" + "others/" + file)


except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
