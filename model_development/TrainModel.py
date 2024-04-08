from torch.nn import CrossEntropyLoss
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision.transforms import Compose, ToTensor, Normalize, RandomHorizontalFlip, RandomVerticalFlip
from torchvision.datasets import CIFAR10
from torch import no_grad, save, load, max as max_t
from os import getcwd
from os.path import join
from operator import __add__
from AlgaeCNN import AlgaeCNN

N_WORKERS = 8
BATCH = 4
EPOCHS = 1
SAVE_DIR = join(getcwd(), "model_weights")

TRANSFORM = Compose([ToTensor(),
                     RandomHorizontalFlip(),
                     RandomVerticalFlip(),
                     Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

TRAIN_SET = CIFAR10(root = getcwd(), train = True, transform = TRANSFORM)
TEST_SET = CIFAR10(root = getcwd(), train = False, transform = TRANSFORM)

def train(model, name, epoch = EPOCHS):
    model.to(model.device)
    loss_f, opt = CrossEntropyLoss(reduction = "sum"), Adam(model.parameters(), lr = 1e-5, eps = 1e-7)

    # loop over the dataset multiple times
    for e in range(epoch):
        running_loss = 0.0
        for i, data in enumerate(DataLoader(TRAIN_SET, shuffle = True, num_workers = N_WORKERS, batch_size = BATCH), 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data[0].to(model.device), data[1].to(model.device)

            # zero the parameter gradients
            opt.zero_grad()

            # forward + backward + optimize
            outputs = model(inputs)
            loss = loss_f(outputs, labels)
            loss.backward()
            opt.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print(f"[{e + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}")
                running_loss = 0.0

    model_path = f"{join(SAVE_DIR, name)}"
    save(model.state_dict(), model_path)
    print(f"Model saved to {model_path}")

def test(model, name):
    correct, total, model_path = 0, 0, f"{join(SAVE_DIR, name)}"
    model.to(model.device)
    model.load_state_dict(load(model_path))
    print(f"Model loaded from {model_path}")
    
    # since we're not training, we don't need to calculate the gradients for our outputs
    with no_grad():
        for data in DataLoader(TEST_SET, shuffle = False, num_workers = N_WORKERS, batch_size = BATCH):
            images, labels = data[0].to(model.device), data[1].to(model.device)
            
            # calculate outputs by running images through the network
            outputs = model(images)
            
            # the class with the highest energy is what we choose as prediction
            _, predicted = max_t(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Network accuracy on 10000 test images: {100 * correct // total}%")
    
if __name__ == "__main__":
    model = AlgaeCNN()
    train(model, "test_model3.pt")
    test(model, "test_model3.pt")