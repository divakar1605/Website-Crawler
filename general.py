import os

# Each website you crawl is a seperate folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory '+directory)
        os.makedirs(directory)

# Create queue and crawled data files
def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

# Create a new file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()


# Delete the contents of a file
def delete_file_data(path):
    with open(path,'w'):
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name,'r') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")

