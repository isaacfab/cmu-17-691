import torchvision
import torchvision.transforms as transforms

train_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

val_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


model = torchvision.models.resnet18(weights=torchvision.models.ResNet18_Weights.IMAGENET1K_V1)
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transform)
valset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=val_transform)
testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=val_transform)