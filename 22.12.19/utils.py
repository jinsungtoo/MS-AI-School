# train loop
# val loop
# 모델 save
# 평가 함수
import torch
import os
import torch.nn as nn
from collections import defaultdict
from tqdm import tqdm
from metric_monitor_temp import MetricMonitor

def calculate_acc(output, target):
    # 평가 함수
    output = torch.sigmoid(output) >= 0.5
    target = target == 1.0
    return torch.true_divide((output == target).sum(dim=0), output.size(0)).item()


def save_model(model, save_dir, file_name="last.pt"):
    # save model
    os.makedirs(save_dir, exist_ok=True)
    output_path = os.path.join(save_dir, file_name)
    if isinstance(model, nn.DataParallel):
        print("멀티 GPU 저장 !! ")
        torch.save(model.module.state_dict(), output_path)
    else:
        print("싱글 GPU 저장 !! ")
        torch.save(model.state_dict(), output_path)

#train loop
def train(train_loader, model, criterion, optimizer, epoch,device) :
    metric_monitor = MetricMonitor()
    model.train()
    stream = tqdm(train_loader)
    for batch_idx, (image, target) in enumerate(train_loader):
        images = image.to(device)
        target = target.to(device)
        output = model(images)
        loss = criterion(output, target)
        accuracy = calculate_acc(output, target)

        metric_monitor.update("Loss", loss.item())
        metric_monitor.update("Accuracy", accuracy.item())
        optimizer.zero_grad() #초기화
        loss.backward()
        optimizer.step()

        stream.set_description(
            f"Epoch : {epoch}. Train... {metric_monitor}".format(
                epoch=epoch, metric_monitor=metric_monitor
            )
        )

# val loop
def validate(val_loader, model, criterion, epoch, device):
    metric_monitor = MetricMonitor()
    model.eval()
    stream = tqdm(val_loader)
    for batch_idx, (image, target) in enumerate(val_loader):
        images = image.to(device)
        target = target.to(device)
        output = model(images)
        loss = criterion(output, target)
        accuracy = calculate_acc(output, target)

        metric_monitor.update("Loss", loss.item())
        metric_monitor.update("Accuracy", accuracy.item())
        stream.set_description(
            f"Epoch : {epoch}. Val... {metric_monitor}".format(
                epoch=epoch, metric_monitor=metric_monitor
            )
        )