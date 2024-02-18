





# Best strategy:
## COPY FILES INTO NEW DIRECTORY WITH THE DESIRED FILENAME (BETTER BE SAFE THEN SORRY!)

```bash
#!/bin/bash

  

# Create the new directory

mkdir ./fixed_filenames

  

# Loop through all files ending with "...1_LoudnessConfig Copy.wav"

for file in *1_LoudnessConfig\ Copy.wav; do

    # Get the new filename by removing the suffix

    new_filename="${file%1_LoudnessConfig Copy.wav}"

  

    # Remove "Thom_Thom_" from the start of the filename

    new_filename="${new_filename#Thom_Thom_}"

  
  

    # Clone the file into the new directory with the new filename

    cp "$file" "./fixed_filenames/$new_filename.wav"

done
```



# Alternative *I don't give a shit* strategy:

### Mutate filenames without duplicating them (UNSAFE!)

```bash
#!/bin/bash

  

# Specify the directory where the files are located

directory="."

  

# Specify the prefix to remove

prefix="Thom_"

  

# Loop through all files in the directory

for file in "$directory"/*; do

    # Check if the file starts with the specified prefix

    if [[ $(basename "$file") == "$prefix"* ]]; then

        # Remove the prefix from the file name

        new_name=$(basename "$file" | sed "s/^$prefix//")

        # Rename the file

        mv "$file" "$directory/$new_name"

    fi

done

```
