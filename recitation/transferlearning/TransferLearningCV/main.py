import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from tqdm import tqdm
import torch.utils.data as data
# from datasets import trainset, valset, testset
import wandb
import logging

def get_model(num_classes):
    # Load the pre-trained model
    model = torchvision.models.resnet18(weights=torchvision.models.ResNet18_Weights.IMAGENET1K_V1)

    # Freeze all layers except the last layer
    for param in model.parameters():
        param.requires_grad = False
    model.fc.requires_grad = True

    # Replace the last layer
    model.fc = nn.Linear(model.fc.in_features, num_classes)

    return model

def evaluate_model(model, dataloader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data in tqdm(dataloader):
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy: %.3f' % (100 * correct / total))

if __name__ == '__main__':

    wandb.login(key=os.environ["WANDB_API_KEY"])
    wandb.init(project="MLIP")
    logging.basicConfig(filename='download.log', level=logging.INFO)

    train_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    val_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Step 1: Load the datasets
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, transform=train_transform)
    valset = torchvision.datasets.CIFAR10(root='./data', train=False, transform=val_transform)
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, transform=val_transform)

    trainset_small = data.Subset(trainset, range(10000))
    trainloader = torch.utils.data.DataLoader(trainset_small, batch_size=32, shuffle=True, num_workers=2)
    
    valset_small = data.Subset(valset, range(1000))
    valloader = torch.utils.data.DataLoader(valset_small, batch_size=32, shuffle=False, num_workers=2)

    # Step 2: Model
    model = get_model(num_classes=10)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    lr_scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

    # Step 3: Training
    num_epochs = 10
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print('Training the model...')
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, data in enumerate(tqdm(trainloader)):
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)

            # IMPORTANT
            optimizer.zero_grad()   # clear gradients of all parameters
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()     # computes the gradients of all the model parameters
            optimizer.step()    # updates the model parameters using the gradients
            running_loss += loss.item()
        
        print('Epoch %d, Loss: %.3f' % (epoch + 1, running_loss / len(trainloader)))
        
        # Step 4: Evaluating
        correct = 0
        total = 0
        with torch.no_grad():
            for data in tqdm(valloader):
                images, labels = data
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        print('Epoch %d, Validation Accuracy: %.3f' % (epoch + 1, 100 * correct / total))
        wandb.log({'train_loss': running_loss / len(trainloader), 'validation_acc': 100 * correct / total})
        
        lr_scheduler.step()

    print('Finished Training')

    # Step 5: Evaluation on the test set
    testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False, num_workers=2)

    print('Evaluating the model on the test set...')
    evaluate_model(model, testloader, device)