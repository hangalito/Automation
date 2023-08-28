from painter import Painter
from subprocess import run
from pathlib import Path
import pprint
import sys
import os


class Organize:
    AUDIO = 'audio'
    COMPRESSED = 'compressed'
    DOCUMENT = 'document'
    IMAGE = 'image'
    VIDEO = 'video'
    SCRIPTS = 'programming'

    def __init__(self, folder, option) -> None:
        self.path = folder
        self.option = option
        home = Path.home()
        home_folders = os.listdir(home)

        for file in home_folders:
            if not os.path.isdir(file):
                home_folders.remove(file)

        if self.path not in home_folders:
            print(Painter(f"The directory {self.path} does not exist").red())
            print(Painter(f"Choose one of the following directories").bold())
            pprint.pprint(home_folders, depth=10, width=90, sort_dicts=True, compact=True)
            quit()
    
    def organize(self):
        answers = ['Y', 'N']
        content = self.filter(os.listdir(Path(self.path).absolute()))
        audios = self.groupByType(content, self.AUDIO)
        images = self.groupByType(content, self.IMAGE)
        videos = self.groupByType(content, self.VIDEO)
        documents = self.groupByType(content, self.DOCUMENT)
        scripts = self.groupByType(content, self.SCRIPTS)
        compressed = self.groupByType(content, self.COMPRESSED)

        def printout(word, count):
            print()
            print(Painter(f"The following {self.pluralize(word, count)} will be moved to the {word.title()} directory").yellow())

        def dislpayChanes(group, word):
            if group:
                printout(word, len(group))
                pprint.pprint(group, indent=2, underscore_numbers=True)

        if option == '-s':
            self.listFiles(self.path)
        elif not option:
            print("The following changes will be applied")

            dislpayChanes(audios, 'audio')
            dislpayChanes(images, 'image')
            dislpayChanes(videos, 'video')
            dislpayChanes(documents, 'document')
            dislpayChanes(scripts, 'code script')
            dislpayChanes(compressed, 'compressed file')
            while True:
                answer = str(input("\nWould you like to continue? Y/N: ")).upper()
                if answer not in answers:
                    continue
                elif answer == answers[-1]:
                    print(Painter("Operation aborted").red(True))
                    quit()
                else:
                    print()
                    break

        if images:
            self.move(images, Path.home().joinpath('Pictures'))
        if videos:
            self.move(videos, Path.home().joinpath('Videos'))
        if audios:
            self.move(audios, Path.home().joinpath('Musics'))
        if documents:
            self.move(documents, Path.home().joinpath('Documents'))
        if scripts:
            self.move(scripts, Path.home().joinpath('Script Codes'))
        if compressed:
            self.move(compressed, 'Compressed Files')
       
        print(Painter("The operation was successfully completed").green(bold=True))

    def move(self, fileList, folder):
        try:
            folder = Path.home().joinpath(folder)
            if folder == 'Pictures':
                if folder not in os.listdir(Path.home()):
                    destination = 'Imagens'
                else:
                    destination = folder
            elif folder == 'Videos':
                if folder not in os.listdir(Path.home()):
                    destination = 'Vídeos'
                else:
                    destination = folder
            elif folder == 'Music':
                if folder not in os.listdir(Path.home()):
                    destination = 'Músicas'
                else:
                    destination = folder
            elif folder == 'Documents':
                if folder not in os.listdir(Path.home()):
                    destination = 'Documentos'
                else:
                    destination = folder
            elif folder == 'Compressed Files':
                if folder not in os.listdir(Path.home()):
                    destination = 'Ficheiros Comprimidos'.title()
                else:
                    destination = folder
            else:
                try:
                    os.mkdir(Path.home().joinpath(folder))
                    destination = folder
                except FileExistsError:
                    destination = folder

            for file in fileList:
                Path.rename(
                    Path(self.path).joinpath(file),
                    destination.joinpath(file)
                )
        except:
            print(destination)
            print(Painter("Couldn't complete the task. Please run the command again to complete the task").yellow())
            quit()

    def countFiles(self, fileList, fileType) -> int | None:
        total = 0

        def lookup(group):
            nonlocal total
            for file in  fileList:
                if self.getFileExtension(file, group) in self.getFormat(group):
                    total += 1

        if fileType is self.AUDIO:
            lookup(self.AUDIO)

        elif fileType is self.COMPRESSED:
            lookup(self.COMPRESSED)

        elif fileType is self.DOCUMENT:
            lookup(self.DOCUMENT)

        elif fileType is self.IMAGE:
            lookup(self.IMAGE)

        elif fileType is self.VIDEO:
            lookup(self.VIDEO)

        elif fileType is self.SCRIPTS:
            lookup(self.SCRIPTS)

        else:
            total = None
        
        return total

    def filter(self, fileList) -> list:
        for file in fileList:
            if file.startswith('.'):
                fileList.remove(file)
        return fileList

    def getFileExtension(self, file, fileType) -> str:
        for extension in self.getFormat(fileType):
            if file.endswith(extension):
                return extension

    def getFormat(self, fileType) -> list:
        if fileType is self.AUDIO:
            return [
                '.mp3',
                '.ogg',
                '.m4a',
            ]        
        elif fileType is self.COMPRESSED:
            return [
                '.7z', '.tar', '.tar.xz',
                '.gz', '.rar', '.zip',
            ]        
        elif fileType is self.DOCUMENT:
            return [
                '.db', '.doc', '.docx',
                '.dotx', '.opd', '.ods',
                '.odt', '.ott', '.pdf',
                '.pps', '.ppsx', '.ppt',
                '.pptx', '.txt', '.xls',
                '.xlsx', '.xltx',
            ]        
        elif fileType is self.IMAGE:
            return [
                '.jpg', '.jpeg', '.tiff',
                '.png', '.gif', '.svg',
            ]
        elif fileType is self.VIDEO:
            return [
                '.mp4', '.mkv', '.wav',
                'webm'
            ]
        elif fileType is self.SCRIPTS:
            return [
                '.c', '.cpp', '.css',
                '.html', '.java', '.js',
                '.json', '.kt', '.php',
                 '.py', '.pyw', '.sql',
                '.swift', '.xml'
            ]
        else:
            return []

    def groupByType(self, files, fileType) -> list:
        list_of_files = []

        def group(thisType):
            for file in files:
                if self.getFileExtension(file, thisType) in self.getFormat(thisType):
                    list_of_files.append(file)

        if fileType is self.AUDIO:
            group(self.AUDIO)
        elif fileType is self.COMPRESSED:
            group(self.COMPRESSED)
        elif fileType is self.DOCUMENT:
            group(self.DOCUMENT)
        elif fileType is self.IMAGE:
            group(self.IMAGE)
        elif fileType is self.VIDEO:
            group(self.VIDEO)
        elif fileType is self.SCRIPTS:
            group(self.SCRIPTS)
        else:
            list_of_files = None
        return list_of_files

    def listFiles(self, folder) -> None:
        countDir = 0
        content_of_this_folder = self.filter(os.listdir(Path(folder).absolute()))
        audioFiles = self.countFiles(content_of_this_folder, self.AUDIO)
        compressedFiles = self.countFiles(content_of_this_folder, self.COMPRESSED)
        documentFiles = self.countFiles(content_of_this_folder, self.DOCUMENT)
        imageFiles = self.countFiles(content_of_this_folder, self.IMAGE)
        videoFiles = self.countFiles(content_of_this_folder, self.VIDEO)
        scpriptFiles = self.countFiles(content_of_this_folder, self.SCRIPTS)
        
        def printout(text: str, number):
            print(Painter(f"{number} {self.pluralize(text, number)}").bold(), end=' ')

        if content_of_this_folder:
            for file in content_of_this_folder:
                if os.path.isdir(Path(folder).joinpath(file)):
                    content_of_this_folder.remove(file)
                    countDir += 1
            pprint.pprint(content_of_this_folder)
            print()
            print(Painter("This folder contains").bold(), end=' ')
            if audioFiles:
                printout("audio", audioFiles)
            if imageFiles:
                printout("image", imageFiles)
            if videoFiles:
                printout("video", videoFiles)
            if documentFiles:
                printout("document", documentFiles)
            if scpriptFiles:
                printout("code script", scpriptFiles)
            if compressedFiles:
                printout("compressed file", compressedFiles)
            if countDir:
                printout("folder", countDir)
            print('')
        else:
            print(Painter("This folder does not have any files or folders").yellow(bold=True))
        quit()

    def pluralize(self, word, count):
        if count == 1:
            return word
        else:
            return word + "s"


############## ENTRY POINT ###############
if len(sys.argv) < 2:
    print(Painter("Usage: python3 organize.py <folder-name> [OPTION]").red(bold=True))
else:
    try:
        try:
            option = sys.argv[2]
        except IndexError:
            option = None

        folder = sys.argv[1]
        organizer = Organize(folder, option)
        organizer.organize()
    except KeyboardInterrupt:
        print(Painter("\nOperation aborted!").red(True))
