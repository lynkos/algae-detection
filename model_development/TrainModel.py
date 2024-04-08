from torch.nn import CrossEntropyLoss
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision.transforms import Compose, ToTensor, Normalize, RandomHorizontalFlip, RandomVerticalFlip
from torchvision.datasets import CIFAR10
from torch import no_grad, save, load, max as max_t
from os import getcwd
from operator import __add__
from AlgaeCNN import AlgaeCNN

N_WORKERS = 8
BATCH = 4
EPOCHS = 1

transform = Compose([ToTensor(),
                     RandomHorizontalFlip(),
                     RandomVerticalFlip(),
                     Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = CIFAR10(root = getcwd(), train = True, transform = transform)
testset = CIFAR10(root = getcwd(), train = False, transform = transform)
trainloader = DataLoader(trainset, shuffle = True, num_workers = N_WORKERS, batch_size = BATCH)
testloader = DataLoader(testset, shuffle = False, num_workers = N_WORKERS, batch_size = BATCH)

def train(model, epoch = EPOCHS, save_path = f"{getcwd()}/test_model3.pt"):
    loss_f, opt = CrossEntropyLoss(reduction = "sum"), Adam(model.parameters(), lr = 1e-5, eps = 1e-7)
    model.to(model.device)

    for e in range(epoch):  # loop over the dataset multiple times
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
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
                print(f'[{e + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                running_loss = 0.0

    print('Finished Training... Saving model...')
    save(model.state_dict(), save_path)

def test(model, load_path = f"{getcwd()}/test_model3.pt"):
    correct, total = 0, 0
    model.load_state_dict(load(load_path))
    model.to(model.device)
    
    # since we're not training, we don't need to calculate the gradients for our outputs
    with no_grad():
        for data in testloader:
            images, labels = data[0].to(model.device), data[1].to(model.device)
            # calculate outputs by running images through the network
            outputs = model(images)
            # the class with the highest energy is what we choose as prediction
            _, predicted = max_t(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the network on the 10000 test images: {100 * correct // total}%')
    
if __name__ == '__main__':
    model = AlgaeCNN()
    #train(model)
    test(model)