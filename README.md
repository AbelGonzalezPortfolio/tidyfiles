# TidyFiles

TidyFiles let's your organize your files based on the file's metadata. It is specially useful when used after recovering data from a hard drive using carvers like photorec. 

## How it works

After opening TidyFiles, select an input and output folder. FileType will then look at each file and determine the mimetype based on the file's headers using the ~filetype~ library. Based on the files the following will occur:

If it is an image, TidyFiles will extract the exif info using the pillow package. The images will be moved to a new folder inside output under the  mimetype / Camera Make / Camera Model 

If no exif info is found the files will go into output / mimetype / no_exif

Videos will be analyzed as above.

Any other filetype will just go into it's mimetype. 

## Why use this

When recovring files from a dead hard drive using a carver like photorec; you are left with a mess of files. This tools helps you sort it based on file information. 

## How to use:

1. Go to our release page and download the latest executable. 
2. Run the executable and select an input and output folder. 
3. Click Start! and let the magic happen. 


## Contribution

Abel Gonzalez 

Star my program if you found it useful! 