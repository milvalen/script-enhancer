import sys

if len(sys.argv) != 2:
    print('Usage: python word_counter.py <file_path>')
else:
    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            print('Number of words:', len(file.read().split()))
    except FileNotFoundError:
        print('File not found:', file_path)   
