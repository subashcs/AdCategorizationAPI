# AdCategorization Model
Categorizes ads based on text content
## Tools Used
  - Python 3.11.5
## Input 
 Text content
## Output
Category of the text (post)

## Training model locally
1. Clone the repository
2. Create a virtual env and run
```
pip install -r requirement.txt
```
3. Download the `GoogleNews-vectors-negative300.bin.gz` data file and keep it on the root directory of the project. 
4. You can run the jupyter notebook `trainingModel.ipynb` file on any supporting editor or jupyter notebook itself.

## Running the API 
To run the API locally, you need to run the flask server using command:
```
python main.py
```

## License
A comparative study of text categorization for advertisement classification © 2019 by Subash Chandra Sapkota is licensed under CC BY 4.0. 
To view a copy of this license, visit LICENSE file.
