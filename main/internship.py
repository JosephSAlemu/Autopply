from datasets import load_dataset, Image

def logOn():
    dataset = load_dataset("monroex/login-screen-dataset")
    test = dataset['train'][1]
    print(test)
    #Use CV in order to detect and find sign in buttons
    
if __name__ == "__main__":
    logOn()